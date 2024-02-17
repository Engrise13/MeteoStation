# Libraries
import datetime # Not used
import sys # Used in ImportError 

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
    data = bt_data.readline().decode().strip()
    string_data_list = data.split()
    float_data_list = []
    for x in string_data_list:
        float_data_list.append(float(x))
    #time = datetime.datetime.now() # Not used
    #ftime = time.strftime("[%Y:%m:%d]-[%H:%M:%S]") # Not used
    with open("src/database.txt", "a") as db:
        db.write(f"{float_data_list[0]} ") # Temperature
        db.write(f"{float_data_list[1]} ") # Humidity
        db.write(f"{float_data_list[2]}\n") # Compute Heat Index
