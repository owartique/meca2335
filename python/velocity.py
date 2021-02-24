# LMECA2335 - Biorobotics
# RHex - Gr4

import numpy as np 
from matplotlib import pyplot as plt 

# Flags
plot = True
save2file = True

# Velocity profile paramters issued from Fig. 2 of komsuoglu paper
phi_s = 0.75	 # sweep angle [rad], ref = 0.75
phi_0 = 0		 # leg offset [rad], ref = 0.35
dc    = 0.3	     # duty cycle, ref = 0.3

# Velocity profile is divided in three segments
# Coordinates of some useful points
ax = -1
ay = -1

bx = -dc
by = phi_0-phi_s/2

cx = dc
cy = phi_0+phi_s/2

dx = 1
dy = 1

# Segment 1 from a to b
s1_A = (by-ay)/(bx-ax)
s1_B = -s1_A*ax + ay

s1_x = np.linspace(ax,bx,1000)
s1_y = s1_A*s1_x + s1_B

# Segment 2 from b to c
s2_A = (cy-by)/(cx-bx)
s2_B = -s2_A*bx + by

s2_x = np.linspace(bx,cx,1000)
s2_y = s2_A*s2_x + s2_B

# Segment 3 from c to d
s3_A = (dy-cy)/(dx-cx)
s3_B = -s3_A*cx + cy

s3_x = np.linspace(cx,dx,1000)
s3_y = s3_A*s3_x + s3_B


# Make one array from the three segments
v_normalized = np.concatenate((s1_y,s2_y))
v_normalized = np.concatenate((v_normalized,s3_y))

# Save values to a txt file
np.savetxt('output.txt',v_normalized)

# Plot
plt.figure()
plt.plot(np.linspace(-1,1,v_normalized.size),v_normalized,'r')
plt.title("Normalized velocity profile")
plt.xlabel("theta/pi")
plt.ylabel("theta/pi")
plt.grid(True)
if plot : plt.show()









