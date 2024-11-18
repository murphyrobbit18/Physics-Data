import numpy as np 
import matplotlib.pyplot as plt

springDef = np.array([0.025, 0.042, 0.06, 0.077, 0.094])
force  = np.array([1, 2.02, 3.03, 4.08, 5.05])

plt.plot(springDef, force, marker = "o")

plt.xlabel('Spring Deformation (m))')
plt.ylabel("Force (N))")
plt.title("Spring Deformation (m) Vs Force (N)")
plt.legend(['Force (N)'])

plt.show()