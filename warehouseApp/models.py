from django.db import models
from accountsApp.models import User
from farmarApp.models import FarmerProfile, Crop

class WarehouseProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50)
    storage_capacity = models.DecimalField(max_digits=12, decimal_places=2)
    location = models.CharField(max_length=100)
    
    def str(self):
        return f"{self.user.username} - {self.location}"

class StockIn(models.Model):
    warehouse = models.ForeignKey(WarehouseProfile, on_delete=models.CASCADE)
    farmer = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price_per_kg = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField(auto_now_add=True)
    
    def str(self):
        return f"StockIn - {self.crop.name} - {self.quantity}kg"

class StockOut(models.Model):
    warehouse = models.ForeignKey(WarehouseProfile, on_delete=models.CASCADE)
    retailer = models.ForeignKey('retailerapp.RetailerProfile', on_delete=models.CASCADE)
    stock_in = models.ForeignKey(StockIn, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price_per_kg = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField(auto_now_add=True)
    
    def str(self):
        return f"StockOut - {self.stock_in.crop.name} - {self.quantity}kg"