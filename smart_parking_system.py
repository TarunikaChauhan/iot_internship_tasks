import requests
import time

# Replace with your Arduino's IP address and port
arduino_ip = "your_arduino_ip"
arduino_port = "your_arduino_port"

# Replace with your server URL or IP address
server_url = "http://your_server_ip_or_domain/parking_status.php"

def get_parking_status():
    try:
        # Send a request to the Arduino to get the parking status
        response = requests.get(f"http://{arduino_ip}:{arduino_port}/get_parking_status")
        return response.text.strip()  # Assuming the response is either "occupied" or "vacant"
    except requests.exceptions.RequestException as e:
        print("Error getting parking status from Arduino:", e)
        return None

def send_parking_status(status):
    payload = {"status": status}
    try:
        response = requests.post(server_url, data=payload)
        print("Server response:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error sending parking status:", e)

def loop():
    while True:
        parking_status = get_parking_status()
        if parking_status is not None:
            send_parking_status(parking_status)
        time.sleep(1)

if __name__ == "__main__":
    print("Smart Parking System - IoT based Car Parking Management")
    try:
        loop()
    except KeyboardInterrupt:
        print("Exiting...")
