import numpy as np 
import matplotlib.pyplot as plt

work = np.array([0.164, 0.297, 0.437, 0.655, 0.741])
energy  = np.array([0.134, 0.253, 0.456, 0.644, 0.745])

plt.plot(work, energy, marker = "o")

plt.xlabel('Work (J)')
plt.ylabel("Kinetic Energy (J)")
plt.title("Work (J) Vs Kinetic Energy (J)")
plt.legend(['Kinetic Energy (J)'])

plt.show()