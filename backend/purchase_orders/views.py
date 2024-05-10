from rest_framework import generics, mixins

from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer

# Create your views here.


class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PurchaseOrderSerializer
    
    def get_queryset(self):
        queryset = PurchaseOrder.objects.all()

        vendor = self.request.query_params.get("vendor")
        print(self.kwargs)
        if vendor:
            filtered_queryset = queryset.filter(vendor=vendor)
            return filtered_queryset
        return queryset


class PurchaseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_field = 'po_number'


