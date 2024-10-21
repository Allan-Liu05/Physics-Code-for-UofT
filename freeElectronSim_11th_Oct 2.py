import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.integrate import odeint

# Constants
FWHM = 350e-15  # FWHM in fs
I_peak = 100  # Peak intensity
P_constant = 9.52e10  # Constant in P(I)
sigma = FWHM / 2.355  # Convert FWHM to sigma for Gaussian

# Time array in femtoseconds
time_fs = np.linspace(0, 350, 1000) 
time_ps = time_fs / 1000  # Convert time to picoseconds for rate equation

# Define the Gaussian function for I(t)
def I_t(t, I_peak, sigma):
    return I_peak * np.exp(-((t - 175e-15) ** 2) / (2 * sigma ** 2))  # Center at 175 fs

# Define P(I) as a function of time
def P_I(t):
    I = I_t(t, I_peak, sigma)
    return P_constant * I**8 * 1e3
    
def avalanche(t):
    I = I_t(t, I_peak, sigma)
    return I

def rate_equation(n, t):
    return 4*avalanche(t)*n 

t = np.linspace(0,350,1000)*1e-15

n_t = odeint(rate_equation, 1, t)
plt.plot(t*1e15,n_t)
plt.show()


# # Solve the differential equation using solve_ivp
# n_t = odeint(P_I, n0, time_fs)

# # Plot the solution
# plt.figure(figsize=(8, 6))
# plt.plot(time_fs, n_t, label='n(t)', color='blue')
# plt.xlabel('Time (fs)')
# plt.ylabel('n(t)')
# plt.title('Evolution of n(t) over 350 fs')
# plt.grid(True)
# plt.legend()
# plt.show()