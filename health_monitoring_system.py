import requests
import time
import random

# Replace with the server URL or IP address to send data
server_url = "http://your_server_ip_or_domain/health_data"

def generate_health_data():
    # Simulate generating health data (blood pressure, sugar level, and heartbeat)
    # Replace this with actual code to read data from sensors in your hardware setup
    blood_pressure = random.randint(100, 140)  # Simulate systolic blood pressure (mmHg)
    sugar_level = random.uniform(80, 150)  # Simulate blood sugar level (mg/dL)
    heartbeat = random.randint(60, 100)  # Simulate heart rate (bpm)
    return blood_pressure, sugar_level, heartbeat

def send_data_to_server(data):
    # Send health data to the server using HTTP POST request
    try:
        response = requests.post(server_url, json=data)
        if response.status_code == 200:
            print("Data sent successfully to the server!")
        else:
            print("Failed to send data. Error code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Failed to send data:", e)

def main():
    while True:
        # Generate simulated health data
        blood_pressure, sugar_level, heartbeat = generate_health_data()
        
        # Create a dictionary with the health data
        data_to_send = {
            "blood_pressure": blood_pressure,
            "sugar_level": sugar_level,
            "heartbeat": heartbeat,
        }

        # Send data to the server
        send_data_to_server(data_to_send)

        time.sleep(60)  # Send data every 60 seconds

if __name__ == "__main__":
    main()
