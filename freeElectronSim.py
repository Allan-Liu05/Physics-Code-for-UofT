import matplotlib as plt
import math

# parameter declarations
wavelength = 1030 * pow(10, -9)
frequency = 2.9106063883 * pow(10,14)
c = 299792458
electron_charge = 1.602176634 * pow(10, -19)
electron_mass = 9.1093837139 * pow (10, -31) #kilogram
reduced_planck = 6.582119569 * pow (10, -16) #electron volt
# band_gap = 9.4 to 9.9 google says 8.96
band_gap = 9.4
# 300 fs laser pulse
energy = 1 # temp value
eosc = ((electron_charge**2)*(energy**2))/(4*electron_mass*(frequency**2))
nph = band_gap/(reduced_planck*frequency)
cw = 1 # temp value
boltzmann_constant = 1.380649*pow(10,-23) # J/K
p_exchange = (3/2)*cw*((boltzmann_constant*293.15)/reduced_planck) #293.15 is assumed room temperature
wmpi = (frequency*(nph**1.5))*((eosc/(2*band_gap))**nph)
wimp = (eosc/band_gap)*((frequency**2*p_exchange)/(p_exchange**2+frequency**2))


free_atom = 8.67 * pow(10,10)
def electron_density(free_electron, time):
    na_term = free_atom*wmpi/wimp
    one_minus = 1-math.exp(-1*wimp*time)
    return (free_electron + na_term*one_minus)*(math.exp(wimp*t))
