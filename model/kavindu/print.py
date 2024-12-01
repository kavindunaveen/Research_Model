import sqlite3
from datetime import datetime, timedelta

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

# Fetch data for the time ranges of the last 4 years
for start_time, end_time in time_ranges:
    cursor.execute("""
        SELECT * FROM kavinduapp_environmentaldata
        WHERE time1 >= ? AND time2 <= ?
    """, (start_time, end_time))

    # Fetch the rows for the current time range
    data = cursor.fetchall()

    # Print the data for this time range if any rows exist
    if data:
        print(f"Data for the time range {start_time} to {end_time}:")
        print("Year | Time Range | Temperature Max | Temperature Min | Humidity Max | Humidity Min | Lux Level Max | Lux Level Min | Soil Moisture Max | Soil Moisture Min | CO2 Max | CO2 Min")
        print("-" * 150)

        for row in data:
            # Assuming your columns are in this order based on your data structure:
            # (id, time1, time2, temperature_max, temperature_min, humidity_max, humidity_min, lux_level_max, lux_level_min, soil_moisture_max, soil_moisture_min, co2_max, co2_min)
            time1 = row[1]
            time2 = row[2]
            temperature_max = row[3]
            temperature_min = row[4]
            humidity_max = row[5]
            humidity_min = row[6]
            lux_level_max = row[7]
            lux_level_min = row[8]
            soil_moisture_max = row[9]
            soil_moisture_min = row[10]
            co2_max = row[11]
            co2_min = row[12]

            # Extract the year from the time1 field
            year = time1[:4]

            # Print the data in a readable format
            print(f"{year} | {time1} to {time2} | {temperature_max:.2f} | {temperature_min:.2f} | {humidity_max:.2f} | {humidity_min:.2f} | {lux_level_max:.2f} | {lux_level_min:.2f} | {soil_moisture_max:.2f} | {soil_moisture_min:.2f} | {co2_max:.2f} | {co2_min:.2f}")
        print("\n" + "="*150 + "\n")

# Close the connection
conn.close()
