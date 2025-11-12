from django.db import models
from accountsApp.models import User

class Crop(models.Model):
    name = models.CharField(max_length=100)  
    season = models.CharField(max_length=50)
    
    def str(self):
        return f"{self.name} - {self.season}"

class FarmerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nid_number = models.CharField(max_length=20)
    land_area = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)  # District/Upazila
    
    def str(self):
        return f"{self.user.username} - {self.location}"

class Cultivation(models.Model):
    farmer = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    season = models.CharField(max_length=50)
    cultivation_cost = models.DecimalField(max_digits=12, decimal_places=2)
    expected_yield = models.DecimalField(max_digits=10, decimal_places=2)
    sowing_date = models.DateField()
    harvest_date = models.DateField()
    
    def str(self):
        return f"{self.farmer.user.username} - {self.crop.name}"