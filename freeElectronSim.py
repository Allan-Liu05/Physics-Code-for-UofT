import matplotlib.pyplot as plt
import math
import numpy as np 
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
w_mpi = 7.809699e14#6.381677e16

electron_mass = 9.1093837e-31 #kg
electron_charge = 1.60217663e-19 #C
reduced_planck_eV = 6.582119569e-16 #eV
reduced_planck_J = 1.054571814e-34 #J
boltzmann_constant_eV = 8.617333262e-5 #eV
boltzmann_constant_J = 1.380649e-23 #J
bohr_radius = 5.29e-11
e_osc_eV = 19 #according to Jingsen, but I calculate 9.866eV
laser_angular_freq = 1.83e15

FWHM = 175  # FWHM in fs
I_peak = 100  # Peak intensity
P_constant = 9.52e10  # Constant in P(I)
sigma = FWHM / 2.355  # Convert FWHM to sigma for Gaussian

# Define the Gaussian function for I(t)
def I_t(t, I_peak, sigma):
    return I_peak * np.exp(-((t - 175) ** 2) / (2 * sigma ** 2))  # Center at 175 fs

def P_I(t):
    I = I_t(t, I_peak, sigma)
    return P_constant * I**8 *1e12

#Scipy approach - seems to be working

def dndt(t, ne):
    return 4*P_I(t)*ne + P_I(t) - ne
ne0 = 0

t = np.linspace(0, 300*pow(10,-15), 30000)
sol = solve_ivp(dndt, t_span=(0, max(t)), y0=[ne0], t_eval=t, method="RK45")
rho = sol.y[0]
plt.plot(t, rho)
plt.show()
plt.close()


# free_e = 2.2e25
# free_ion = 2.2e25
# dt = 1e-15
# delta = []
# wimp = w_imp(free_e)
# beta = 5.06336e-27

# for t in range(4700):
#     free_e = dt*(free_e*wimp - beta*free_ion*(free_e**2))
#     free_ion = free_ion - free_e
#     delta.append(free_e)
#     wimp = w_imp(free_e)
#     print("free electron = " + str(free_e) + " free_ion = " + str(free_ion) + " wimp = " + str(w_imp))

# time = [x for x in range(len(delta))]
# plt.plot(time, delta)
# plt.show()
# plt.close()

