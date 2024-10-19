import matplotlib.pyplot as plt
import math
import numpy as np 
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
w_mpi = 7.292721e14 #7.809699e14 assuming nph = 5.8, but photons are discrete so i use 6

electron_mass = 9.1093837e-31 #kg
electron_charge = 1.60217663e-19 #C
reduced_planck_eV = 6.582119569e-16 #eV
reduced_planck_J = 1.054571814e-34 #J
boltzmann_constant_eV = 8.617333262e-5 #eV
boltzmann_constant_J = 1.380649e-23 #J
bohr_radius = (reduced_planck_J**2)/(electron_mass*(electron_charge**2))
e_osc_eV = 20 #9.86637 #eV or 1.8659e15 depending on equation used
laser_angular_freq = 1.83e15




# Gaussian function for intensity
def gaussian_intensity(t):
    FWHM = 350e-15  # FWHM in seconds (350 fs)
    I_0 = 1e14      # Peak intensity in W/cm^2
    t_0 = 175e-15         # Center of the Gaussian pulse, at t = 0
    return (I_0 * np.exp(-4 * np.log(2) * (t - t_0)**2 / FWHM**2))/1e12 # /1e12 to get TW/cm^2

def multiphoton(t):
    return (9.523e10 * (gaussian_intensity(t)**8))*1e12

rho = []
t = np.linspace(0,350,3500)*1e-15
ne = 0
for dt in t:
    print(ne/150e-15)
    ne = multiphoton(dt) + 4*multiphoton(dt)*ne - (ne/(1e-15))
    rho.append(ne)

# def dndt(t, ne):
#     tau = 1e-15

#     return 4*multiphoton(t)*ne + multiphoton(t) - (ne/tau)
# ne0 = 0
# t = np.linspace(0, 350*pow(10,-15), 30000)
# sol = solve_ivp(dndt, t_span=(0, max(t)), y0=[ne0], t_eval=t, method="Radau")
# rho = sol.y[0]

plt.plot(t*1e15, rho)
plt.grid(True)
plt.show()
plt.close()
