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
boltzmann_constant_eV = 8.617333262-5 #eV
boltzmann_constant_J = 1.380649e-23 #J
bohr_radius = (reduced_planck_J**2)/(electron_mass*(electron_charge**2))
e_osc_eV = 20 #9.86637 #eV or 1.8659e15 depending on equation used
laser_angular_freq = 1.83e15

free_atoms = 8.67e10 #quantity of free atoms initially that can be ionized
def cw(current_electron_density):
    return 0.31*math.pi*bohr_radius*(current_electron_density**1/3)

def p_exchange(current_electron_density):
    return (3*cw(current_electron_density)*boltzmann_constant_J*273.15)/(2*reduced_planck_J)

def w_imp(current_electron_density):
    eV_term = e_osc_eV/9.0 #9.0eV is the band gap of SiO2
    rate_term_numerator = ((laser_angular_freq)**2)*p_exchange(current_electron_density)
    rate_term_denominator = (p_exchange(current_electron_density)**2) + (laser_angular_freq**2)
    rate_term = rate_term_numerator/rate_term_denominator
    return eV_term*rate_term

# def free_electron_density(current_electron_density, free_atom_count, time):
#     if(current_electron_density == 0):
#         return free_atom_count*w_mpi
#     if(free_atom_count == 0):
#         return current_electron_density*w_imp(current_electron_density)
#     rate_term = (free_atom_count*w_mpi)/w_imp(current_electron_density)
#     negative_exponential = 1-math.exp(-1*w_imp(current_electron_density)*time)
#     positive_exponential = math.exp(w_imp(current_electron_density)*time)
#    # print(str(rate_term) + " " + str(negative_exponential) + " " + str(positive_exponential))
#     return (current_electron_density + rate_term*negative_exponential)*positive_exponential

# delta_electron_density = []
# current_free_electron_count = 0
# current_free_atom_count = 8.67e10
# for t in range(30):
#     time = t*pow(10,-17)
#     free_electron_count = free_electron_density(current_free_electron_count, current_free_atom_count, time)
#     current_free_atom_count = current_free_atom_count - free_electron_count
#     delta_electron_density.append(free_electron_count)

# xs = [x for x in range(len(delta_electron_density))]
# plt.plot(xs, delta_electron_density)
# plt.show()
# plt.close()

#Scipy approach - seems to be working
current_free_atom_count = 8.67e10
def dndt(t, ne):
    na = current_free_atom_count - ne
    if (na <= 0):
        na = 0
    
    return ne*w_imp(ne) + na*w_mpi
ne0 = 0

t = np.linspace(0, 300*pow(10,-15), 30000)
sol = solve_ivp(dndt, t_span=(0, max(t)), y0=[ne0], t_eval=t, method="RK45")
rho = sol.y[0]
plt.plot(t, rho)
plt.show()
plt.close()


