from . import views
from django.urls import path

urlpatterns = [
    path('', views.PurchaseOrderListCreateAPIView.as_view()),
    path('<str:po_number>/', views.PurchaseRetrieveUpdateDestroyAPIView.as_view()),
]
