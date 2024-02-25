# Libraries
import sys  # Used in ImportError, SerialException
import argparse

# CLI Parser
parser = argparse.ArgumentParser()

parser.add_argument(
    "-d",
    "--rfcomm-device",
    default="/dev/rfcomm0",
    help="Choose different RFCOMM device for Bluetooth connection.",
)

parser.add_argument(
    "-b",
    "--baud-rate",
    type=int,
    default=9600,
    help="Change BAUD rate of connection.",
)

args = parser.parse_args()

# Serial Import
try:
    import serial
except ImportError:
    sys.exit('ERROR: Install "pyserial" library first!')

# Bluetooth Init
try:
    bt_data = serial.Serial(args.rfcomm_device, args.baud_rate)  # Bluetooth connection
    print("Initialization Successful")
except serial.SerialException:
    sys.exit(
        "Error: Serial Exception - Check your BAUD rate, RFCOMM device, and your Bluetooth connection."
    )

# Writing readings to DB
while True:
    data = bt_data.readline().decode().strip().split()
    float_data_list = []
    for x in data:
        if x != "nan":
            float_data_list.append(float(x))
    try:
        with open("database.txt", "a") as db:
            db.write(f"{float_data_list[0]} ")  # Temperature
            db.write(f"{float_data_list[1]} ")  # Humidity
            db.write(f"{float_data_list[2]}\n")  # Compute Heat Index
    except IndexError:
        continue
