from django.db import models
from django.db.models.functions import Now

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=120)                         #CharField - Vendor's name.
    contact_details = models.TextField(blank=True, null=True)       #TextField - Contact information of the vendor.
    address = models.TextField(blank=True, null=True)               #TextField - Physical address of the vendor.
    vendor_code = models.CharField(max_length=120, unique=True)     #CharField - A unique identifier for the vendor.
    on_time_delivery_rate = models.FloatField(default=0)            #FloatField - Tracks the percentage of on-time deliveries.
    quality_rating_avg = models.FloatField(default=0)               #FloatField - Average rating of quality based on purchase orders.
    average_response_time = models.FloatField(default=0)            #FloatField - Average time taken to acknowledge purchase orders.
    fulfillment_rate = models.FloatField(default=0)                 #FloatField - Percentage of purchase orders fulfilled successfully.

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey("vendors.Vendor", on_delete=models.CASCADE)  #ForeignKey - Link to the Vendor model.
    date = models.DateTimeField(default=Now())                              #DateTimeField - Date of the performance record.
    on_time_delivery_rate = models.FloatField(default=0)                    #FloatField - Historical record of the on-time delivery rate.
    quality_rating_avg = models.FloatField(default=0)                       #FloatField - Historical record of the quality rating average.
    average_response_time = models.FloatField(default=0)                    #FloatField - Historical record of the average response time.
    fulfillment_rate = models.FloatField(default=0)                         #FloatField - Historical record of the fulfilment rate.

