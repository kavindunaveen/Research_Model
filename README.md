# 🌿 Smart Greenhouse IoT Project 🌱

Welcome to the **Smart Greenhouse IoT Project**, an innovative system that integrates IoT, machine learning, and energy-efficient technologies to revolutionize traditional farming practices. This project focuses on optimizing environmental parameters in a greenhouse using real-time monitoring, automated control, and predictive analytics, ensuring enhanced plant growth and sustainable agriculture.

---

## 🚀 Project Overview

The **Smart Greenhouse IoT Project** addresses challenges in traditional greenhouse management by automating critical systems such as climate control, lighting, energy, and irrigation. Leveraging advanced IoT devices, sensors, and machine learning models, the system dynamically adjusts environmental parameters to maintain ideal conditions for plant growth while minimizing energy usage and human intervention.

---

## 🌟 Key Features

### **Real-Time Monitoring**
- Sensors measure temperature, humidity, soil moisture, light intensity, and water levels.
- Data is sent to the cloud for real-time access and analysis.

### **Automated Control**
- Actuators (fans, pumps, lights, humidifiers, and solenoid valves) respond automatically to sensor data to optimize conditions.

### **Energy Efficiency**
- Machine learning models predict and adjust environmental settings to save energy and reduce carbon footprints.

### **Remote Accessibility**
- A web dashboard allow users to monitor and control the system from anywhere.

### **User Notifications**
- Alerts notify users when environmental parameters deviate from predefined thresholds or when adjustments are made.

---

## 📘 Research Questions

1. How can IoT-based systems optimize climate control, lighting, energy, and irrigation in greenhouses?
2. How does integrating machine learning improve energy efficiency and sustainability in greenhouse operations?
3. What is the impact of automated systems on plant growth and resource management?

---

## 🎯 Objectives

1. Implement an IoT-based system for real-time monitoring and control of greenhouse parameters.
2. Automate climate control, lighting, and irrigation systems using predictive analytics.
3. Optimize energy usage to reduce greenhouse operational costs and environmental impact.
4. Provide a user-friendly dashboard for manual and automated system management.
5. Evaluate the system's performance in improving plant growth and resource efficiency.

---

## 📊 System Workflow

1. **Data Collection**: Sensors gather data on temperature, humidity, soil moisture, water levels, and light intensity.
2. **Data Processing**: The ESP32 microcontroller processes sensor data and sends it to Firebase for cloud storage.
3. **Automation**: Actuators are triggered based on predefined thresholds and machine learning predictions.
4. **Manual Override**: Users can control actuators via a web dashboard.
5. **Notifications**: Alerts are sent for parameter deviations or system adjustments.

---

## 🔧 Tools and Technologies

### **IoT and Hardware**
- **Microcontroller**: ESP32
- **Sensors**:
  - DHT11: Measures temperature and humidity.
  - Ultrasonic Sensor: Monitors water levels.
  - Float Sensor: Detects water presence.
  - BH1750: Measures light intensity.
- **Actuators**:
  - Fans, humidifiers, solenoid valves, water pumps, and LED lighting systems.

### **Cloud and Backend**
- **Firebase**: Real-time data storage and remote control.
- **Django Framework**: Backend system for web applications and dashboards.

### **Machine Learning**
- **scikit-learn**: Predicts optimal environmental conditions based on historical data.

### **Visualization and Notifications**
- **Chart.js**: Interactive data visualization on the dashboard.
- **Twilio**: Sends SMS notifications to users.

### **Database**
- SQLite: Stores historical sensor data and predictions.

---

## 🔄 System Diagram

The following diagram illustrates the system's architecture:

![System Diagram](https://drive.google.com/uc?id=1dhIlv7QAJmPtYJb74kv8VG2FebXt8eGp)

---

## 🛠️ Project Phases

| **Phase**       | **Description**                                                                             |
|------------------|---------------------------------------------------------------------------------------------|
| **1. Research**        | Define objectives, identify challenges, and design the system architecture.            |
| **2. Design**          | Develop hardware diagrams, select components, and create software structure.          |
| **3. Development**     | Assemble hardware, write firmware, and test individual modules.                       |
| **4. Integration**     | Combine hardware and software, integrate machine learning, and implement automation.  |
| **5. Testing**         | Test the system for reliability, usability, and performance.                          |
| **6. Deployment**      | Deploy the system in a greenhouse environment for real-world validation.              |

---

## 📜 Current Progress

| **Task**                     | **Status**        |
|------------------------------|-------------------|
| Hardware Setup               | Completed         |
| Sensor Integration           | Completed         |
| Database Connection          | Completed         |
| Manual Control via Dashboard | In Progress       |
| Automation Logic             | In Progress       |
| Dashboard Development        | In progress           |

---

## 🔮 Future Enhancements

1. **Dashboard Development**: Add advanced analytics and real-time data visualization.
2. **Notifications**: Improve notifications with detailed alerts and insights.
3. **Energy Optimization**:
   - Further reduce energy usage through dynamic adjustments.
   - Explore renewable energy integration.
4. **Scalability**: Optimize the system for large-scale greenhouses.

---

## 👨‍💻 Team Members and Roles

- **Malshika A.I**: Climate control and predictive analytics.
- **Weerasingha W.A.N.S**: Lighting system design and automation.
- **Premathilakage K.N.P**: Energy management and dashboard development.
- **Abeyweera M.P.C.S**: Irrigation system and real-time adjustments based on soil moisture data.

**Supervisors**:
- Mrs. Thamali Kelegama (Faculty of Computing)
- Ms. Aparna Jayawardena (Assistant Lecturer)

---

## 🤝 Contributing

We welcome contributions! If you'd like to contribute to this project, please submit a pull request or open an issue.

---

## 📱 Contact

For inquiries or suggestions, feel free to reach out via email or GitHub issues.
