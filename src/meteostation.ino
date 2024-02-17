// Libraries
#include <DHT.h> 
#include <SoftwareSerial.h> 

// Init
SoftwareSerial bluetooth(2,3); 
DHT dht(4, DHT22);

// Setup
void setup() { 
  dht.begin();
  bluetooth.begin(9600);
}

// Loop
void loop() {
  float t = dht.readTemperature(); // Temperature
  float h = dht.readHumidity(); // Humidity
  float th = dht.computeHeatIndex(t, h, false); // Compute Heat Index
  bluetooth.print(t);
  bluetooth.print(" ");
  bluetooth.print(h);
  bluetooth.print(" ");
  bluetooth.print(th);
  bluetooth.print("\n");
  delay(1000);
}
