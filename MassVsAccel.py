import numpy as np 
import matplotlib.pyplot as plt

mass = np.array([0.3, 0.425, 0.55, 0.675])
accel  = np.array([1.3, 0.998, 0.686, 0.504])

plt.plot(mass, accel, marker = "o")

plt.xlabel('Mass (kg)')
plt.ylabel("Acceleration (m/s/s)")
plt.title("Mass (kg) Vs Acceleration (m/s/s)")
plt.legend(['Acceleration (m/s/s)'])

plt.show()