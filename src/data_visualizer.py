# Libraries
import sys # Used in ImportError 

try:
    import matplotlib.pyplot as plt
except ImportError:
    print('ERROR: Install "matplotlib" library first!')
    sys.exit()

try:
    import numpy as np
except ImportError:
    print('ERROR: Install "numpy" library first!')
    sys.exit()

# Init
heat_index_list = []
with open("src/database.txt", "r") as file:
    for line in file:
        values = line.strip().split()
        if values:
            last_value = float(values[2]) # 0 - Temperature, 1 - Humidity, 2 - Heat Index
            heat_index_list.append(last_value)

readings_list = list(range(1, len(heat_index_list) + 1))

# Plot creation
plt.plot(np.array(readings_list), np.array(heat_index_list))
plt.xlabel('Number of Readings')
plt.ylabel('Compute Heat Index')
plt.title('Compute Heat Index Graph')
plt.grid(True)
plt.show()
