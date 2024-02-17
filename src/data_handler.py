# Libraries
import sys # Used in ImportError, SerialException

try:
    import serial
except ImportError:
    print('ERROR: Install "pyserial" library first!')
    sys.exit()

# Init
try:
    bt_data = serial.Serial('/dev/rfcomm0', 9600) # Bluetooth connection
    print("Initialization Successful")
except serial.SerialException:
    print("ERROR: Connect to HC05 via Bluetooth")
    sys.exit()

# Writing readings to DB
while True:
    data = bt_data.readline().decode().strip().split()
    float_data_list = []
    for x in data:
        if x == 'nan':
            continue
        else:
            float_data_list.append(float(x))

    with open("src/database.txt", "a") as db:
        db.write(f"{float_data_list[0]} ") # Temperature
        db.write(f"{float_data_list[1]} ") # Humidity
        db.write(f"{float_data_list[2]}\n") # Compute Heat Index