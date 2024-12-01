from django.db import models

class EnvironmentalData(models.Model):
    # Primary key field will be automatically created by Django as 'id'
    id = models.AutoField(primary_key=True)
    
    # Time-related fields
    time1 = models.DateTimeField()
    time2 = models.DateTimeField()

    # Environmental parameters
    temperature_max = models.FloatField()
    temperature_min = models.FloatField()
    humidity_max = models.FloatField()
    humidity_min = models.FloatField()
    lux_level_max = models.FloatField()
    lux_level_min = models.FloatField()
    soil_moisture_max = models.FloatField()
    soil_moisture_min = models.FloatField()
    co2_max = models.FloatField()
    co2_min = models.FloatField()

    def __str__(self):
        return f"EnvironmentalData at {self.time1} - Temp: {self.temperature_max}/{self.temperature_min}, Humidity: {self.humidity_max}/{self.humidity_min}"


