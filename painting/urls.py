from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('api/', include('customer.urls')),
    path('api/', include('postproduct.urls')),
    path('api/',include('salesman.urls')),
    path('api/', include('notification.urls')),
    path('api/',include('chat.urls')),
    path('api/', include('products.urls')),
    path('api/',include('products.urls')),
    path('api/',include('realestate.urls')),
    path('backend/',include('electronic.urls')),
    path('backend/',include('car.urls')),
    path('backend/',include('food.urls')),
    path('appliance/',include('appliance.urls')),
    path('beauty/' ,include('beauty.urls')),
    path('wedding/',include('wedding.urls')),
    path('enter/', include('entertainment.urls')),
    path('travel/', include('travel.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   



