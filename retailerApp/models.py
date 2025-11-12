from django.db import models
from accountsApp.models import User

class RetailerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=100)
    trade_license = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    
    def str(self):
        return f"{self.shop_name} - {self.user.username}"

class RetailerStock(models.Model):
    retailer = models.ForeignKey(RetailerProfile, on_delete=models.CASCADE)
    stock_out = models.ForeignKey('warehouseapp.StockOut', on_delete=models.CASCADE)
    selling_price_per_kg = models.DecimalField(max_digits=8, decimal_places=2)
    is_approved = models.BooleanField(default=False)
    
    def str(self):
        return f"RetailerStock - {self.retailer.shop_name}"