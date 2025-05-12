
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('api/', include('customer.urls')),
    path('api/', include('postproduct.urls')),
    path('api/',include('salesman.urls')),
    path('api/', include('notification.urls')),
    path('admin/', admin.site.urls),
]




