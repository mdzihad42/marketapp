from django.db import models
from accountsApp.models import User
from retailerApp.models import RetailerProfile
from farmarApp.models import Crop

class MarketScanReport(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'MONITORING_AGENT'})
    retailer = models.ForeignKey(RetailerProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Crop, on_delete=models.CASCADE)
    reported_price = models.DecimalField(max_digits=8, decimal_places=2)
    photo_evidence = models.ImageField(upload_to='market_scans/')
    datetime = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    
    def str(self):
        return f"MarketScan - {self.retailer.shop_name} - {self.product.name}"