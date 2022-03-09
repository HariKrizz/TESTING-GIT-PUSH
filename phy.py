import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dn2/db2
def model(n,b):
d2ndb2 = 2*(-0.00317 + 0.0030270) + 12 * 0.0000281 * b**2 + 24*(b - (0.035)**-4)*(-0.000077 - 2 * 0.0000018 * 1/(b**2-0.035))

# initial condition
c0 = 1.450
c1 = -0.00317
c2 = 0.0000281
c3 = 0.0030270
c4 = -0.000077
c5 = 0.0000018
l = 0.035


# time points
n = np.linspace(0,n)

# solve ODE
y = odeint(model,c0,t) 

# plot results
plt.plot(t,y)
plt.xlabel('lambda0 (b)')
plt.ylabel('ng * 1e8')
plt.show()