from django.db import models
from warehouseApp.models import StockOut
from retailerApp.models import RetailerProfile

class Transport(models.Model):
    company_name = models.CharField(max_length=100)
    vehicle_number = models.CharField(max_length=20)
    driver_details = models.TextField()
    
    def str(self):
        return f"{self.company_name} - {self.vehicle_number}"

class DeliveryChalan(models.Model):
    STATUS_CHOICES = (
        ('dispatched', 'Dispatched'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )
    
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE)
    stock_out = models.OneToOneField(StockOut, on_delete=models.CASCADE)
    source_warehouse = models.ForeignKey('warehouseapp.WarehouseProfile', on_delete=models.CASCADE)
    destination_retailer = models.ForeignKey(RetailerProfile, on_delete=models.CASCADE)
    dispatch_time = models.DateTimeField()
    received_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='dispatched')
    
    def str(self):
        return f"DeliveryChalan - {self.stock_out.id}"