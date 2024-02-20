# MeteoStation v1.0
Simple `Arduino`-`Python` project utilizing `DHT-22` and `HC-05` modules to measure and send **humidity**, **temperature**, and **Compute Heat Index** (with `DHT-22` module) via bluetooth (with `HC-05` module)

## Components Needed
- `Arduino (UNO)` - Arduino Board
- `DHT-22` - Temperature/Humidity sensor
- `HC-05` - Bluetooth Data Transmitter
- `Breadboard` - For connecting everything together
- `Wires` - For connecting everything together

## Installation Guide
1) Run `pip install -r requirements.txt`
2) Set your Arduino board and sensors up
3) Connect to `HC-05` via bluetooth
4) Download and extract the `.zip` file
5) Download `DHT.h` and `SoftwareSerial.h`
6) Verify and Upload `meteostation` 
7) Run `data_handler` to get readings, and `data_visualizer` to show the graph based on the readings you got
8) Enjoy and feel free to modify it!

## Working Principle Breakdown
1) `DHT22` sensor gets temperature and humidity values
2) These values are sent to your PC via `HC-05` bluetooth module
3) They are handled and get added to a database by `data_handler`
4) You can see the graph (that takes data from the database) via `data_visualizer`

## Future Plans
- Notification system (via Telegram)
- MicroSD support
- Temperature Trends & Predictions
- Real-time Graph & API 
- Code improvements :white_check_mark:
