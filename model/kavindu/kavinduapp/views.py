from django.shortcuts import render
from datetime import datetime, timedelta
import sqlite3
from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timedelta
from .models import EnvironmentalData
from django.shortcuts import render
from .models import EnvironmentalData
from datetime import datetime, timedelta
from django.utils import timezone




def environmental_data_view(request):
    # Get current time and calculate the time range
    current_time = datetime.now()
    start_time = current_time.replace(minute=0, second=0, microsecond=0)  # Set time to 00 minutes of the hour
    end_time = start_time + timedelta(hours=1)  # The time range is 1 hour

    # Calculate the same time range for the past 4 years
    time_ranges = []
    for i in range(4):
        year_time_range = (start_time.replace(year=current_time.year - i), end_time.replace(year=current_time.year - i))
        time_ranges.append(year_time_range)

    # Connect to the SQLite database
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Initialize the data dictionary to store results
    data_per_year = {}

    # Fetch data for the time ranges of the last 4 years
    for start_time, end_time in time_ranges:
        cursor.execute("""
            SELECT * FROM kavinduapp_environmentaldata
            WHERE time1 >= ? AND time2 <= ?
        """, (start_time, end_time))

        # Fetch the rows for the current time range
        data = cursor.fetchall()

        # Add the data to the dictionary by year
        year = start_time.year
        if data:
            # Format numerical values to 2 decimal points
            formatted_data = [
                [round(value, 2) if isinstance(value, (float, int)) else value for value in row]
                for row in data
            ]
            data_per_year[year] = formatted_data

    # Close the connection
    conn.close()

    # Pass the data to the template
    return render(request, 'index.html', {'data_per_year': data_per_year, 'current_time': current_time})
def temperature_chart(request):
    # Get the current date and time
    current_time = datetime.now()
    
    # Get the date and time from 30 days ago
    start_date = current_time - timedelta(days=30)
    
    # Query the last 30 records, ordered by time1
    records = EnvironmentalData.objects.filter(time1__gte=start_date).order_by('-time1')[:30]
    
    # Prepare data for the chart
    labels = []
    temperature_max = []
    temperature_min = []

    # Populate the labels and data arrays
    for record in records:
        labels.append(record.time1.strftime('%Y-%m-%d %H:%M:%S'))  # Format time1 as a string
        temperature_max.append(record.temperature_max)
        temperature_min.append(record.temperature_min)
    
    # Reverse the lists to show them in chronological order (oldest to newest)
    labels.reverse()
    temperature_max.reverse()
    temperature_min.reverse()

    # Return the data as JSON
    return JsonResponse({
        'labels': labels,
        'temperature_max': temperature_max,
        'temperature_min': temperature_min
    })



def humidity(request):
    # Get the current date and time
    current_time = datetime.now()
    
    # Get the date and time from 30 days ago
    start_date = current_time - timedelta(days=30)
    
    # Query the last 30 records, ordered by time1
    records = EnvironmentalData.objects.filter(time1__gte=start_date).order_by('-time1')[:30]
    
    # Prepare data for the chart
    labels = []
    temperature_max = []
    temperature_min = []

    # Populate the labels and data arrays
    for record in records:
        labels.append(record.time1.strftime('%Y-%m-%d %H:%M:%S'))  # Format time1 as a string
        temperature_max.append(record.temperature_max)
        temperature_min.append(record.temperature_min)
    
    # Reverse the lists to show them in chronological order (oldest to newest)
    labels.reverse()
    temperature_max.reverse()
    temperature_min.reverse()

    # Return the data as JSON
    return JsonResponse({
        'labels': labels,
        'temperature_max': temperature_max,
        'temperature_min': temperature_min
    })

def humidity(request):
    # Get the current date and time
    current_time = datetime.now()
    
    # Get the date and time from 30 days ago
    start_date = current_time - timedelta(days=30)
    
    # Query the last 30 records, ordered by time1
    records = EnvironmentalData.objects.filter(time1__gte=start_date).order_by('-time1')[:30]
    
    # Prepare data for the chart
    labels = []
    humidity_max = []
    humidity_min = []

    # Populate the labels and data arrays
    for record in records:
        labels.append(record.time1.strftime('%Y-%m-%d %H:%M:%S'))  # Format time1 as a string
        humidity_max.append(record.humidity_max)
        humidity_min.append(record.humidity_min)
    
    # Reverse the lists to show them in chronological order (oldest to newest)
    labels.reverse()
    humidity_max.reverse()
    humidity_min.reverse()

    # Return the data as JSON
    return JsonResponse({
        'labels': labels,
        'humidity_max': humidity_max,
        'humidity_min': humidity_min
    })



def luxlevel(request):
    # Get the current date and time
    current_time = datetime.now()
    
    # Get the date and time from 30 days ago
    start_date = current_time - timedelta(days=30)
    
    # Query the last 30 records, ordered by time1
    records = EnvironmentalData.objects.filter(time1__gte=start_date).order_by('-time1')[:30]
    
    # Prepare data for the chart
    labels = []
    lux_level_max = []
    lux_level_min = []

    # Populate the labels and data arrays
    for record in records:
        labels.append(record.time1.strftime('%Y-%m-%d %H:%M:%S'))  # Format time1 as a string
        lux_level_max.append(record.lux_level_max)
        lux_level_min.append(record.lux_level_min)
    
    # Reverse the lists to show them in chronological order (oldest to newest)
    labels.reverse()
    lux_level_max.reverse()
    lux_level_min.reverse()

    # Return the data as JSON
    return JsonResponse({
        'labels': labels,
        'lux_level_max': lux_level_max,
        'lux_level_min': lux_level_min
    })


def soil(request):
    # Get the current date and time
    current_time = datetime.now()
    
    # Get the date and time from 30 days ago
    start_date = current_time - timedelta(days=30)
    
    # Query the last 30 records, ordered by time1
    records = EnvironmentalData.objects.filter(time1__gte=start_date).order_by('-time1')[:30]
    
    # Prepare data for the chart
    labels = []
    soil_moisture_max = []
    soil_moisture_min = []

    # Populate the labels and data arrays
    for record in records:
        labels.append(record.time1.strftime('%Y-%m-%d %H:%M:%S'))  # Format time1 as a string
        soil_moisture_max.append(record.soil_moisture_max)
        soil_moisture_min.append(record.soil_moisture_min)
    
    # Reverse the lists to show them in chronological order (oldest to newest)
    labels.reverse()
    soil_moisture_max.reverse()
    soil_moisture_min.reverse()

    # Return the data as JSON
    return JsonResponse({
        'labels': labels,
        'soil_moisture_max': soil_moisture_max,
        'soil_moisture_min': soil_moisture_min
    })




def co2(request):
    # Get the current date and time
    current_time = datetime.now()
    
    # Get the date and time from 30 days ago
    start_date = current_time - timedelta(days=30)
    
    # Query the last 30 records, ordered by time1
    records = EnvironmentalData.objects.filter(time1__gte=start_date).order_by('-time1')[:30]
    
    # Prepare data for the chart
    labels = []
    co2_max = []
    co2_min = []

    # Populate the labels and data arrays
    for record in records:
        labels.append(record.time1.strftime('%Y-%m-%d %H:%M:%S'))  # Format time1 as a string
        co2_max.append(record.co2_max)
        co2_min.append(record.co2_min)
    
    # Reverse the lists to show them in chronological order (oldest to newest)
    labels.reverse()
    co2_max.reverse()
    co2_min.reverse()

    # Return the data as JSON
    return JsonResponse({
        'labels': labels,
        'co2_max': co2_max,
        'co2_min': co2_min
    })


from django.http import JsonResponse
from django.utils import timezone
import pytz
from datetime import datetime, timedelta
from .models import EnvironmentalData  # Assuming you have the EnvironmentalData model

def dataentry(request):
    # Set timezone to Asia/Colombo
    colombo_tz = pytz.timezone('Asia/Colombo')
    current_time = timezone.now().astimezone(colombo_tz)  # Current time in Asia/Colombo
    in_range_message = []  # This will hold in-range messages
    out_of_range_message = []  # This will hold out-of-range messages

    if request.method == 'POST':
        # Get the form data
        actual_temperature = float(request.POST.get('temperature'))
        actual_humidity = float(request.POST.get('humidity'))
        actual_lux_level = float(request.POST.get('lux_level'))
        actual_soil_moisture = float(request.POST.get('soil_moisture'))
        actual_co2 = float(request.POST.get('co2'))

        year_range = [current_time.year - i for i in range(4)]
        in_range = True  # Assume values are in range initially

        # Loop through the last 4 years and compare the data with the form input
        for year in year_range:
            hour = current_time.hour
            time_start = timezone.make_aware(datetime(year, current_time.month, current_time.day, hour), timezone=colombo_tz)
            time_end = time_start + timedelta(hours=1)

            # Fetch data records for the given time range
            data_records = EnvironmentalData.objects.filter(time1__range=[time_start, time_end])

            if data_records.exists():
                for record in data_records:
                    # Check if values are in range and categorize the messages
                    if not (record.temperature_min <= actual_temperature <= record.temperature_max):
                        out_of_range_message.append(f"Temperature for {year} is not in range.")
                    else:
                        in_range_message.append(f"Temperature for {year} is in range.")
                    
                    if not (record.humidity_min <= actual_humidity <= record.humidity_max):
                        out_of_range_message.append(f"Humidity for {year} is not in range.")
                    else:
                        in_range_message.append(f"Humidity for {year} is in range.")
                    
                    if not (record.lux_level_min <= actual_lux_level <= record.lux_level_max):
                        out_of_range_message.append(f"Lux Level for {year} is not in range.")
                    else:
                        in_range_message.append(f"Lux Level for {year} is in range.")
                    
                    if not (record.soil_moisture_min <= actual_soil_moisture <= record.soil_moisture_max):
                        out_of_range_message.append(f"Soil Moisture for {year} is not in range.")
                    else:
                        in_range_message.append(f"Soil Moisture for {year} is in range.")
                    
                    if not (record.co2_min <= actual_co2 <= record.co2_max):
                        out_of_range_message.append(f"CO2 for {year} is not in range.")
                    else:
                        in_range_message.append(f"CO2 for {year} is in range.")
            else:
                out_of_range_message.append(f"No data available for the time range in {year}.")

        # Determine the message based on whether values are in range or not
        message = "You are in range." if in_range_message else "You are not in range. Details:"

        # Return a JSON response with the message
        return JsonResponse({
            'message': message, 
            'in_range_message': in_range_message, 
            'out_of_range_message': out_of_range_message
        })

    # If it's a GET request, just render the page with the current time
    return render(request, 'index.html', {'current_time': current_time, 'message': message})
