# Libraries
import sys # Used in ImportError 
import math # Used to remove all NaN values

try:
    import serial
except ImportError:
    print('ERROR: Install "pyserial" library first!')
    sys.exit()

# Init
bt_data = serial.Serial('/dev/rfcomm0', 9600) # Bluetooth connection
print("Initialization Successful")

# Writing readings to DB
while True:
    data = bt_data.readline().decode().strip().split()
    float_data_list = []
    for x in data:
        float_data_list.append(float(x))
        
    if all(math.isnan(val) for val in float_data_list):
        continue

    with open("src/database.txt", "a") as db:
        db.write(f"{float_data_list[0]} ") # Temperature
        db.write(f"{float_data_list[1]} ") # Humidity
        db.write(f"{float_data_list[2]}\n") # Compute Heat Index