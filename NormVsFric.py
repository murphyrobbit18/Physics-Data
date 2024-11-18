import numpy as np 
import matplotlib.pyplot as plt

normForce = np.array([1.18, 2.17, 3.16, 4.13, 5.12])
kineticFric  = np.array([0.61, 0.81, 0.97, 1.26, 1.63])
statFric = np.array([0.73, 0.91, 1.45, 1.67, 1.93])

plt.plot(normForce, kineticFric, marker = "o")
plt.plot(normForce, statFric, marker = "o")

plt.xlabel('Normal Force (N)')
plt.ylabel("Friction (N)")
plt.title("Normal Force (N) Vs Friction (N)")
plt.legend(["Kinetic Friction (N)", 'Static Friction (N)'])

plt.show()