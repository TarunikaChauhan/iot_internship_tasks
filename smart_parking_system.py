import requests
import RPi.GPIO as GPIO
import time

# Replace with your server URL or IP address
server_url = "http://your_server_ip_or_domain/parking_status.php"

parking_pin = 18  # GPIO pin for parking sensor

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(parking_pin, GPIO.IN)

def send_parking_status(status):
    payload = {"status": status}
    try:
        response = requests.post(server_url, data=payload)
        print("Server response:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error sending parking status:", e)

def loop():
    while True:
        parking_status = GPIO.input(parking_pin)
        send_parking_status(parking_status)
        time.sleep(1)

def cleanup():
    GPIO.cleanup()

if __name__ == "__main__":
    print("Smart Parking System - IoT based Car Parking Management")
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        cleanup()
