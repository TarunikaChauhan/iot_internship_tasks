#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME680.h>
#include <SoftwareSerial.h>

// Replace with your Wi-Fi credentials
const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";

// Replace with your server URL or IP address
const char* serverURL = "http://your_server_ip_or_domain/health_data.php";

const int heartRateSensorPin = A0;
const int bloodPressureSensorPin = A1;
const int sugarLevelSensorPin = A2;

Adafruit_BME680 bme;  // Initialize the BME680 sensor

void setup() {
  Serial.begin(9600);
  Wire.begin();
  bme.begin(0x76);  // Start the BME680 sensor

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
}

void loop() {
  // Read sensor data
  float heartRate = readHeartRate();
  float bloodPressure = readBloodPressure();
  float sugarLevel = readSugarLevel();
  float temperature = readTemperature();
  float humidity = readHumidity();

  // Send the data to the server
  sendHealthData(heartRate, bloodPressure, sugarLevel, temperature, humidity);

  delay(60000);  // Send data every minute
}

float readHeartRate() {
  // Read data from the heart rate sensor and return the heart rate value
  // You need to implement the specific logic for your heart rate sensor
}

float readBloodPressure() {
  // Read data from the blood pressure sensor and return the blood pressure value
  // You need to implement the specific logic for your blood pressure sensor
}

float readSugarLevel() {
  // Read data from the sugar level sensor and return the sugar level value
  // You need to implement the specific logic for your sugar level sensor
}

float readTemperature() {
  // Read data from the BME680 sensor and return the temperature value
  return bme.readTemperature();
}

float readHumidity() {
  // Read data from the BME680 sensor and return the humidity value
  return bme.readHumidity();
}

void sendHealthData(float heartRate, float bloodPressure, float sugarLevel, float temperature, float humidity) {
  // Prepare payload for POST request
  String payload = "heart_rate=" + String(heartRate) +
                   "&blood_pressure=" + String(bloodPressure) +
                   "&sugar_level=" + String(sugarLevel) +
                   "&temperature=" + String(temperature) +
                   "&humidity=" + String(humidity);

  HTTPClient http;
  http.begin(serverURL);
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");

  int httpResponseCode = http.POST(payload);

  if (httpResponseCode > 0) {
    String response = http.getString();
    Serial.println("Server response: " + response);
  } else {
    Serial.print("Error code: ");
    Serial.println(httpResponseCode);
  }

  http.end();
}
