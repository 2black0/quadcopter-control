import numpy as np
import control as ct
import matplotlib.pyplot as plt

#parameter of DC Motor
L = 0.673   # Motor inductance H
R = 6.5     # Motor resistance Ohm
J = 0.01171 # Motor inertia Kgm^2
Ki = 0.038  # Torque constant Nm/A
Kb = 0.038  # Back emf constant Vs/rad
B = 0.00143 # Viscous friction Nms/rad

A = np.array([[-R/L, 0, -Kb/L],[0, 0, 1], [Ki/J, 0, -B/J]])
B = np.array([[1/L], [0], [0]])
C = np.array([[0, 1, 0]])
D = np.array([[0]])

SS_motor = ct.ss(A, B, C, D)

print('State Space Model of DC Motor\n', SS_motor)

t,y = ct.step_response(SS_motor)

plt.plot(t,y)
plt.grid()
plt.xlabel('Time')
plt.title('Step Response with SS Model')
plt.show()