# Smart Greenhouse Energy Management System

This is a **Smart Greenhouse Energy Management System** that utilizes machine learning models to predict and optimize environmental parameters such as temperature, humidity, and light (lux) levels. The system compares real-time sensor data with historical data to ensure optimal conditions for energy-efficient greenhouse management. 

The system adjusts sensor settings automatically and sends notifications when any environmental condition deviates from its optimal range. The user can also manually control the system remotely through the web dashboard.

### **Key Features:**
- **Automatic Sensor Adjustment**: Sensors for temperature, humidity, and lux are automatically adjusted when data goes above or below the desired thresholds based on historical data.
- **User Notifications**: Users receive notifications on their phones when sensor data goes beyond the high or low range and when automatic adjustments are made.
- **Real-Time Control**: Users can manually control the greenhouse sensor settings remotely through the dashboard, eliminating the need to be physically present.
- **Energy Efficiency**: By monitoring and controlling environmental conditions, the system optimizes energy usage and reduces the carbon footprint of greenhouse operations.

---

## **Technologies Used:**
- **Django**: Backend framework for web application development.
- **Python**: Programming language used for backend logic and machine learning model development.
- **Machine Learning (scikit-learn)**: Predictive models based on past environmental data to determine optimal settings for the greenhouse.
- **Chart.js**: JavaScript library used to render interactive charts for visualizing sensor data and predictions.
- **SQLite**: Database used to store sensor data and predictions.
- **Twilio (for notifications)**: Used to send SMS notifications to users when sensor adjustments are made.
- **JavaScript**: Used for interactive features like data visualization and manual control on the web dashboard.

---

## **Future Work**
**Real-Time Data Integration**:
- The dashboard will be integrated with real-time sensors for continuous data collection.
- The system will update the dashboard in real time with live data and predictions.

**Mobile Notifications (SMS/Email)**:
- Set up Twilio (or another notification service) to send SMS notifications when sensors are adjusted.
- Notifications will include details about what adjustments were made and why.

**Advanced Machine Learning Model**:
- Enhance the ML model with more features (e.g., external weather data, seasonal trends) to improve the accuracy of predictions.
- Retrain the model regularly with new sensor data to keep it up to date.

**Energy Optimization and Carbon Footprint Reduction**:
- The system will be optimized for energy-saving operations by dynamically adjusting the sensor values and maintaining optimal environmental conditions.
- This will help in reducing the carbon footprint of the greenhouse operation.

**Deployment**:
- Deploy the system to a cloud server for remote access and integrate it with real-time sensor hardware.

## **Setup Instructions**

### 1. **Clone the Repository**:
Clone the repository to your local machine:
```bash
##git clone https://github.com/kavindunaveen/Research_Model

2. Set Up the Virtual Environment
A virtual environment isolates your project’s dependencies and allows you to install required packages without affecting your global Python installation.

Create the virtual environment:
##python -m venv greenhouse_env
Activate the virtual environment:
For Windows:
##.\greenhouse_env\Scripts\activate
For macOS/Linux:
##source greenhouse_env/bin/activate

3. Install Dependencies
Install the required Python packages by running:
##pip install -r requirements.txt

4. Database Setup
To create the necessary database tables and migrate the schema, run:
##python manage.py makemigrations
##python manage.py migrate

5. Create a Superuser
To access the Django admin and the app, create a superuser:
##python manage.py createsuperuser

Follow the prompts to create the superuser.

6. Run the Development Server
Start the Django development server:
##python manage.py runserver

Open your browser and navigate to http://127.0.0.1:8000/ to view the application.


