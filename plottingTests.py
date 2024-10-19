import numpy as np
import matplotlib.pyplot as plt

# Parameters
alpha = 1.0  # Example value for alpha
sigma_k = 0.5  # Example value for sigma_k
tau = 2.0  # Example value for tau

# Gaussian function parameters
I0 = 100  # Peak intensity in TW/cm^2
t0 = 0.0  # Center of the Gaussian (assuming it peaks at t = 0 fs)
fwhm = 350e-15  # FWHM in seconds (350 fs)
sigma = fwhm / (2 * np.sqrt(2 * np.log(2)))  # Convert FWHM to sigma

# Gaussian function I(t) in terms of time (assuming t is in seconds)
def I(t):
    return I0 * np.exp(-((t - t0) ** 2) / (2 * sigma ** 2))

def Ik(t):
    return np.cos(t)  # Example: cosine function for Ik(t)

# Time discretization
t_start = -1e-12  # Start time in seconds (assuming 1 ps window)
t_end = 1e-12  # End time in seconds
dt = 1e-15  # Time step size (1 fs)
time_steps = np.arange(t_start, t_end, dt)

# Initial condition
n0 = 0.0  # Set initial value of n(t) to 0
n_values = [n0]  # List to store n values over time

# Euler's method for numerical integration
for t in time_steps[:-1]:
    n = n_values[-1]
    dn_dt = alpha * I(t) * n + sigma_k * Ik(t) - n / tau
    n_new = n + dn_dt * dt
    n_values.append(n_new)

# Plot the result
plt.plot(time_steps * 1e15, n_values)  # Convert time to fs for plotting
plt.xlabel('Time (fs)')
plt.ylabel('n(t)')
plt.title('Numerical Solution with n(0) = 0 and Gaussian I(t)')
plt.show()