from . import views
from django.urls import path

urlpatterns = [
    path('', views.VendorListCreateAPIView.as_view()),                                  #POST /api/vendors/: Create a new vendor. 
                                                                                        #GET /api/vendors/: List all vendors.

    path('<str:vendor_code>/', views.VendorRetrieveUpdateDestroyAPIView.as_view()),     #GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
                                                                                        #PUT /api/vendors/{vendor_id}/: Update a vendor's details.
                                                                                        #DELETE /api/vendors/{vendor_id}/: Delete a vendor.
]

