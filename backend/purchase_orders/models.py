from django.db import models
from django.db.models.functions import Now, TruncDay

# Create your models here.

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=120, unique=True)               #CharField - Unique number identifying the PO.
    vendor = models.ForeignKey("vendors.Vendor", on_delete=models.CASCADE)  #ForeignKey - Link to the Vendor model.
    order_date = models.DateTimeField()                                     #DateTimeField - Date when the order was placed.
    delivery_date = models.DateTimeField()                                  #DateTimeField - Expected or actual delivery date of the order.
    items = models.JSONField()                                              #JSONField - Details of items ordered.
    quantity = models.IntegerField()                                        #IntegerField - Total quantity of items in the PO.
    status = models.CharField(max_length=10)                                #CharField - Current status of the PO (e.g., pending, completed, canceled).
    quality_rating = models.FloatField(default=0, null=True, blank=True)    #FloatField - Rating given to the vendor for this PO (nullable).
    issue_date = models.DateTimeField(null=True, blank=True)                #DateTimeField - Timestamp when the PO was issued to the vendor.
    acknowledgment_date = models.DateTimeField(null=True, blank=True)       #DateTimeField, nullable - Timestamp when the vendor acknowledged the PO.
