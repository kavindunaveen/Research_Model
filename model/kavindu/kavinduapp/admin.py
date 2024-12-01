from django.contrib import admin
from .models import EnvironmentalData

class EnvironmentalDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'time1', 'time2', 'temperature_max', 'temperature_min', 
                    'humidity_max', 'humidity_min', 'lux_level_max', 'lux_level_min', 
                    'soil_moisture_max', 'soil_moisture_min', 'co2_max', 'co2_min')
    list_filter = ('time1', 'time2')  # You can add other fields for filtering if needed
    search_fields = ('id', 'time1', 'time2')  # Allows searching by id, time1, or time2

admin.site.register(EnvironmentalData, EnvironmentalDataAdmin)
