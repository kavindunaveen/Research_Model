![image](https://github.com/user-attachments/assets/7f77b220-1221-4e05-81ca-7f358cb10916)# Smart Greenhouse IoT Project

## Project Overview
The **Smart Greenhouse IoT Project** aims to revolutionize traditional farming practices by introducing a comprehensive and automated solution to monitor and control greenhouse conditions. This project combines **IoT (Internet of Things)** technologies with advanced automation to ensure optimal conditions for plant growth, minimize manual intervention, and increase efficiency.

Our system integrates **real-time monitoring**, **cloud connectivity**, and **remote control** to manage key environmental factors such as temperature, humidity, soil moisture, light intensity, and water levels. By leveraging data-driven insights and automated control systems, this project contributes to sustainable agriculture and resource optimization.

---

## Features of the Smart Greenhouse System
- **Real-Time Data Collection:**
  - Sensors measure temperature, humidity, soil moisture, light intensity, and water levels.
  - Live data is sent to Firebase for analysis and remote access.
  
- **Automation and Control:**
  - Actuators (fans, pumps, humidifiers, solenoid valves) respond to predefined thresholds for automatic climate control.
  - Lighting systems provide supplemental lighting based on light intensity readings.

- **Remote Monitoring and Manual Override:**
  - Users can access real-time data and control the system manually via a mobile app or dashboard.
  
- **Energy Efficiency:**
  - Adaptive climate control minimizes energy consumption while maintaining optimal growing conditions.

---

## Research Questions
1. What is the impact of IoT-based climate control systems in improving efficiency and reducing manual intervention in greenhouses?
2. How can real-time data and automated controls ensure optimal plant growth conditions?

---

## Objectives
1. Develop an IoT-based greenhouse system to optimize plant growth conditions.
2. Automate climate control, irrigation, and lighting systems using real-time data.
3. Provide remote monitoring and control via a mobile app or cloud platform.
4. Evaluate system performance to ensure sustainability and efficiency.

---

## Methodology
1. **Data Collection:**
   - Sensors collect environmental data, including temperature, humidity, water level, and light intensity.
   
2. **Data Processing:**
   - The ESP32 microcontroller processes sensor data and uploads it to Firebase for cloud storage.
   
3. **Automation:**
   - Predefined thresholds trigger actuators for tasks like irrigation, ventilation, and lighting adjustments.
   
4. **Manual Override:**
   - Users can override automation settings and control actuators remotely through a mobile app.
   
5. **Evaluation:**
   - The system is tested for efficiency, usability, and reliability in real-world greenhouse conditions.

---

## System Workflow
1. **Startup:**
   - Connect the system to a power source.
   - Connect the ESP32 microcontroller to Wi-Fi.
   
2. **Data Collection:**
   - Sensors collect environmental data and send it to the microcontroller.
   
3. **Cloud Integration:**
   - Data is transmitted to Firebase for real-time monitoring and storage.
   
4. **Control and Automation:**
   - Based on sensor readings, actuators are triggered automatically.
   - Users can manually override automation via the mobile app.
   
5. **Feedback and Adjustments:**
   - Notifications are sent to users for critical changes (e.g., low water levels, high temperature).
   - Users can make adjustments as needed.

---
## System Diagram

The following diagram illustrates the overall architecture of our Smart Greenhouse IoT system:

![System Diagram](https://drive.google.com/uc?id=1dhIlv7QAJmPtYJb74kv8VG2FebXt8eGp)



## Tools and Technologies
- **Microcontroller:** ESP32
- **Sensors:**
  - DHT11: Measures temperature and humidity.
  - Ultrasonic Sensor: Monitors water levels.
  - Float Sensor: Detects water presence for irrigation.
  
- **Actuators:**
  - Fans, humidifiers, solenoid valves, pumps, and dimmable lights.

- **Cloud Platform:** Firebase for real-time data storage and control.
- **Software Tools:** Arduino IDE, Firebase SDK, Python for additional data analysis.

---

## Work Breakdown Structure
| **Phase**             | **Tasks**                                                                                       |
|-----------------------|------------------------------------------------------------------------------------------------|
| **1. Initialization** | Define objectives, perform literature review, and finalize system design.                      |
| **2. Design**         | Develop hardware diagrams, create component lists, and finalize the software architecture.     |
| **3. Development**    | Assemble hardware components, write firmware, and test individual modules (sensors, actuators).|
| **4. Integration**    | Combine all components, integrate Firebase, and test system automation.                        |
| **5. Testing**        | Evaluate system performance, collect feedback, and optimize for reliability.                   |
| **6. Deployment**     | Deploy the system in a real-world greenhouse environment and monitor performance.              |

---

## Team Members and Roles
- **Malshika A.I:** Implement a real-time feedback system to adjust heating, cooling, and ventilation based on predictive analytics to maintain optimal climate conditions.
- **Weerasingha W.A.N.S:** Lighting system design and automation.
- **Premathilakage K.N.P:** Energy management and mobile app development.
- **Abeyweera M.P.C.S:** System design and overall testing.

**Supervisors:**
- Mrs. Thamali Kelegama, Faculty of Computing
- Ms. Aparna Jayawardena, Assistant Lecturer

---

## Future Enhancements
1. Develop advanced machine learning algorithms for predictive climate control.
2. Expand mobile app features for better user interaction and analytics.
3. Optimize the system for larger-scale applications in commercial greenhouses.

---


