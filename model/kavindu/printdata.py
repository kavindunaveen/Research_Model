import sqlite3
import random
from datetime import datetime, timedelta

# Function to generate random data for the table columns
def generate_random_data(time1):
    # time2 is exactly 1 hour after time1
    time2 = time1 + timedelta(hours=1)

    return {
        'time1': time1,
        'time2': time2,
        'temperature_max': random.uniform(30.0, 40.0),
        'temperature_min': random.uniform(10.0, 20.0),
        'humidity_max': random.uniform(70.0, 90.0),
        'humidity_min': random.uniform(30.0, 50.0),
        'lux_level_max': random.uniform(500.0, 1000.0),
        'lux_level_min': random.uniform(100.0, 300.0),
        'soil_moisture_max': random.uniform(30.0, 60.0),
        'soil_moisture_min': random.uniform(10.0, 30.0),
        'co2_max': random.uniform(400.0, 600.0),
        'co2_min': random.uniform(200.0, 400.0)
    }

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Delete all existing records from the table
cursor.execute("DELETE FROM kavinduapp_environmentaldata")

# Starting time (set to current date with the hour set to 7:00 AM)
current_time = datetime.now().replace(minute=0, second=0, microsecond=0) + timedelta(hours=7)

# Number of records to generate (approx 35040 for 4 years, assuming 1 record per hour)
num_records = 35040

# Inserting random data into the table (going back in time)
for _ in range(num_records):
    data = generate_random_data(current_time)

    cursor.execute(""" 
        INSERT INTO kavinduapp_environmentaldata (
            time1, time2, temperature_max, temperature_min, 
            humidity_max, humidity_min, lux_level_max, lux_level_min, 
            soil_moisture_max, soil_moisture_min, co2_max, co2_min
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data['time1'], data['time2'], data['temperature_max'], data['temperature_min'], 
        data['humidity_max'], data['humidity_min'], data['lux_level_max'], data['lux_level_min'], 
        data['soil_moisture_max'], data['soil_moisture_min'], data['co2_max'], data['co2_min']
    ))

    # Update current_time for the next record (subtract 1 hour for the previous record)
    current_time = current_time - timedelta(hours=1)

# Commit the transaction and close the connection
conn.commit()
conn.close()

print(f"{num_records} random records with continuous time ranges (hourly) have been added to the 'kavinduapp_environmentaldata' table, going back 4 years.")
