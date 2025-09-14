from rest_framework import generics
from .models import RealEstate
from django.http import HttpResponse
from rest_framework.views import APIView
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import views
from rest_framework.response import Response
import json
from .serializers import RealEstateSerializer
from .models import Order, Wallet, Subscription, Refund
from .serializers import OrderSerializer, WalletSerializer, SubscriptionSerializer, RefundSerializer
stripe.api_key = settings.STRIPE_SECRET_KEY
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = RealEstate.objects.all()
    serializer_class = RealEstateSerializer

class PendingOrdersAPIView(generics.ListAPIView):
    queryset = Order.objects.filter(status="pending")
    serializer_class = OrderSerializer

class CompletedOrdersAPIView(generics.ListAPIView):
    queryset = Order.objects.filter(status="completed")
    serializer_class = OrderSerializer


# ----------------- WALLET -----------------
class WalletAPIView(generics.ListAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


# ----------------- SUBSCRIPTIONS -----------------
class SubscriptionsAPIView(generics.ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


# ----------------- REFUNDS -----------------
class RefundsAPIView(generics.ListAPIView):
    queryset = Refund.objects.all()
    serializer_class = RefundSerializer


# ----------------- PAYMENT UPDATES -----------------
class PaymentUpdatesAPIView(APIView):
    def get(self, request):
        orders = Order.objects.all().order_by("-created_at")
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


# ----------------- STRIPE CHECKOUT -----------------
@csrf_exempt
def create_checkout_session(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            line_items = [
                {
                    "price_data": {
                        "currency": "etb",
                        "product_data": {"name": item["name"]},
                        "unit_amount": int(item["price"]) * 100,
                    },
                    "quantity": item["quantity"],
                }
                for item in data.get("items", [])
            ]

            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=line_items,
                mode="payment",
                success_url="https://kenash.shop/forsale",
                cancel_url="https://kenash.shop/cancel",
            )

            # Save as pending order
            for item in data.get("items", []):
                Order.objects.create(
                    stripe_session_id=session.id,
    customer_email=data.get("email", None),
    product_id=item["id"],
    product_name=item["name"],
    description=item.get("description", ""),
    image_url=item.get("image", ""),
    specs=item.get("specs", []),
    quantity=item.get("quantity", 1),
    amount_total=item["price"],
    currency="ETB",
    status="pending",
                )

            return JsonResponse({"id": session.id})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)


# ----------------- STRIPE WEBHOOK -----------------
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except Exception as e:
        return HttpResponse(status=400)

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        Order.objects.filter(stripe_session_id=session["id"]).update(
            status="completed",
            customer_email=session["customer_details"]["email"],
        )

    elif event["type"] == "charge.refunded":
        refund = event["data"]["object"]
        order = Order.objects.filter(stripe_session_id=refund["payment_intent"]).first()
        if order:
            Refund.objects.create(order=order, amount=refund["amount"] / 100, reason="Requested")
            order.status = "refunded"
            order.save()

    return HttpResponse(status=200)