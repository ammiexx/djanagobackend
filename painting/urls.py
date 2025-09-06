from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('api/', include('customer.urls')),
    path('api/', include('postproduct.urls')),
    path('api/',include('salesman.urls')),
    path('api/', include('notification.urls')),
    path('api/',include('chat.urls')),
    path('api/', include('products.urls')),
    path('api/',include('realestate.urls')),
    path('backend/',include('electronic.urls')),
    path('backend/',include('car.urls')),
    path('backend/',include('food.urls')),
    path('appliance/',include('appliance.urls')),
    path('beauty/' ,include('beauty.urls')),
    path('wedding/',include('wedding.urls')),
    path('enter/', include('entertainment.urls')),
    path('travel/', include('travel.urls')),
    path('discounts/',include('dailydiscounts.urls')),
    path('discounts/', include('weeklydiscounts.urls')),
    path('new/', include('newproducts.urls')),
    path('upcomming/', include('upcomming.urls')),
    path('api/',include('message.urls')),
    path('api/', include('education.urls')),
    path('api/', include('maintenance.urls')),
    path('api/', include('agriculture.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   

