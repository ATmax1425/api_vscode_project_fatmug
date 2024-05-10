from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home),
    path('vendors/', include('vendors.urls')),
    path('purchase_orders/', include('purchase_orders.urls'))
]

