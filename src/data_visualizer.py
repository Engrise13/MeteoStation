# Libraries
import sys  # Used in ImportError

try:
    import matplotlib.pyplot as plt
except ImportError:
    sys.exit('ERROR: Install "matplotlib" library first!')

try:
    import numpy as np
except ImportError:
    sys.exit('ERROR: Install "numpy" library first!')

# Init
heat_index_list = []
with open("src/database.txt", "r") as file:
    for line in file:
        values = line.strip().split()
        if values:
            # 0 - Temperature, 1 - Humidity, 2 - Heat Index
            shown_value = float(values[2])
            heat_index_list.append(shown_value)

readings_list = list(range(1, len(heat_index_list) + 1))

# Plot creation
plt.plot(np.array(readings_list), np.array(heat_index_list))
plt.xlabel("Number of Readings")
plt.ylabel("Compute Heat Index")
plt.title("Compute Heat Index Graph")
plt.grid(True)
plt.show()
