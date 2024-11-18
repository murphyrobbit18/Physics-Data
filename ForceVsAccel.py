import numpy as np 
import matplotlib.pyplot as plt

force = np.array([1.96, 1.47, 0.981, 0.491])
accel  = np.array([3.09, 1.88, 0.515, 0.277])

plt.plot(force, accel, marker = "o")

plt.xlabel('Force (N)')
plt.ylabel("Acceleration (m/s/s)")
plt.title("Force (N) Vs Acceleration (m/s/s)")
plt.legend(['Acceleration (m/s/s)'])

plt.show()