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
y = []
with open("src/database.txt", "r") as file:
    for line in file:
        values = line.strip().split()
        if values:
            last_value = float(values[2]) # 0 - Temperature, 1 - Humidity, 2 - Heat Index
            y.append(last_value)

x = list(range(1, len(y) + 1))

# Plot creation
plt.plot(np.array(x), np.array(y))
plt.xlabel('Number of Readings')
plt.ylabel('Compute Heat Index')
plt.title('Compute Heat Index Graph')
plt.grid(True)
plt.show()
