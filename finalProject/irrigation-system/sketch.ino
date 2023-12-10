unsigned long previousMillis = 0;
const unsigned long interval = 3000; // 3 second

int minMoisture = 0; // Minimum moisture level
int maxMoisture = 100; // Maximum moisture level
int lowMoistureThreshold = 30; // Threshold for low moisture
int highMoistureThreshold = 70; // Threshold for high moisture

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  unsigned long currentMillis = millis();

  // decide how to respond when the plant is in different moisture level
  if (currentMillis - previousMillis >= interval) {
    // Generate a random moisture level within the specified range
    int randomMoisture = random(minMoisture, maxMoisture + 1); // Add 1 to include the maximum value
    
    // Print the random moisture level
    Serial.print("Random Moisture Level: ");
    Serial.println(randomMoisture);
    
    // Check if the moisture level is low or high
    if (randomMoisture < lowMoistureThreshold) {
      Serial.println("Moisture level is LOW. Start watering");
    } else if (randomMoisture > highMoistureThreshold) {
      Serial.println("Moisture level is HIGH. Help!!");
    } else {
      Serial.println("Moisture level is NORMAL");
    }
    
    // Reset the timer
    previousMillis = currentMillis;
  }
}
