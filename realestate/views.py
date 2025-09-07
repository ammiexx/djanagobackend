from rest_framework import generics
from .models import RealEstate
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .serializers import RealEstateSerializer
stripe.api_key = settings.STRIPE_SECRET_KEY
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = RealEstate.objects.all()
    serializer_class = RealEstateSerializer

@csrf_exempt  # allow React POST requests
def create_checkout_session(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            line_items = [
                {
                    "price_data": {
                        "currency": "etb",  # Ethiopian Birr
                        "product_data": {"name": item["name"]},
                        "unit_amount": int(item["price"]) * 100,  # convert to cents
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

            return JsonResponse({"id": session.id})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)

