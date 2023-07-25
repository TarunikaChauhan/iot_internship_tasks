import requests
import time

# Replace with your Arduino's IP address
arduino_ip = "your_arduino_ip"
# Replace with the endpoint on the Arduino to get sensor data
sensor_endpoint = "/get_sensor_data"

# Replace with the server URL or IP address to send data
server_url = "http://your_server_ip_or_domain/air_pollution_data"

def read_sensor_data():
    # Implement code to communicate with your Arduino over Wi-Fi or serial (depending on your setup)
    # This function should return the sensor data (e.g., gas concentration, temperature, etc.)
    # Example:
    # gas_concentration = arduino_request(arduino_ip + sensor_endpoint)
    # return gas_concentration

def send_data_to_server(data):
    # Send sensor data to the server using HTTP POST request
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
        sensor_data = read_sensor_data()
        if sensor_data:
            # Process sensor data and create a dictionary with relevant information
            data_to_send = {
                "gas_concentration": sensor_data["gas_concentration"],
                "temperature": sensor_data["temperature"],
                # Add more data as needed
            }
            send_data_to_server(data_to_send)

        time.sleep(60)  # Send data every 60 seconds

if __name__ == "__main__":
    main()
