import numpy as np

#
## Parameters - Dushan to set these ...
#
lat = -33.617778 # Ellsworth 2017, NCC
lon = 150.740278

# leaf transmissivity [-] (VIS: 0.07 - 0.15)
# ENF: 0.05; EBF: 0.05; DBF: 0.05; C3G: 0.070
tau = np.array([0.1, 0.3])

# leaf reflectance [-] (VIS:0.07 - 0.15)
# ENF: 0.062;EBF: 0.076;DBF: 0.092; C3G: 0.11
refl = np.array([0.1, 0.3])

# intercellular concentration of O2 [mmol mol-1]
Oi = 210.0

# CO2 compensation point - base rate at 25 deg C / 298 K [umol mol-1]
gamstar25 = 57.64

# Michaelis-Menten coefficents for carboxylation by Rubisco at
# 25degC [umol mol-1] or 298 K
Kc25 = 404.9

# Michaelis-Menten coefficents for oxygenation by Rubisco at
# 25degC [mmol mol-1]. Note value in Bernacchie 2001 is in mmol!!
# or 298 K
Ko25 = 278.4

# Activation energy for carboxylation [J mol-1]
Ec = 79430.0

# Activation energy for oxygenation [J mol-1]
Eo = 36380.0

# Activation energy at CO2 compensation point [J mol-1]
Eag = 37830.0

Ear = None # 34000.0

# Curvature of the light response.
# See Peltoniemi et al. 2012 Tree Phys, 32, 510-519
theta_hyperbol = 0.9995
#theta = 0.85

# Curvature of the light response (-)
# set to MAESTRA numbers
theta_J = 0.57

quantum_yield = 0.3

absorptance = 1 - refl[0] - tau[0]

# Leaf quantum yield (initial slope of the A-light response curve) [mol mol-1]
# this value (0.246) is slightly lower than MAESTRA (0.26)
# reflectance and transmittance should change to MAESTRA

#alpha = quantum_yield * absorptance # (Medlyn et al 2002)
alpha = 0.24
# residual stomatal conductance as net assimilation rate reaches zero
# (mol m-2 s-1)
g0 = 0.0

# slope of the sensitivity of stomatal conductance to assimilation (mol m-2 s-1)
g1 = 2.43 # WTC3 estimates.

# the sensitivity of stomatal conductance to D (kPa)
D0 = 1.5

# Deactivation energy for Vcmax [J mol-1]
Hdv = 200000.0

# Deactivation energy for Jmax [J mol-1]
Hdj = 200000.0

# max rate of rubisco activity at 25 deg or 298 K
Vcmax25 = 106.96

# potential rate of electron transport at 25 deg or 298 K
Jmax25 = 168.47

# Rspiration rate at the reference temperature 25 deg C or 298 K [deg K]

Rd25 = -0.13

# ratio of respiration at a given temperature divided by respiration
# at a temperature 10 degrees lower
Q10 = 2.0

# activation energy for the parameter [J mol-1]
Eaj = 39676.89

# activation energy for the parameter [J mol-1]
Eav = 82620.87

# entropy factor [J mol-1 K-1)
deltaSj = 641.3615

# entropy factor [J mol-1 K-1)
deltaSv = 634

# leaf width (m)
leaf_width = 0.02

# Cambell & Norman, 11.5, pg 178
# The solar absorptivities of leaves (-0.5) from Table 11.4 (Gates, 1980)
# with canopies (~0.8) from Table 11.2 reveals a surprising difference.
# The higher absorptivityof canopies arises because of multiple reflections
# among leaves in a canopy and depends on the architecture of the canopy.
SW_abs = 0.8 # use canopy absorptance of solar radiation

# leaf emissivity (-), Table 3, Wang and Leuning, 1998
emissivity_leaf = 0.96

# soil emissivity (-), Table 3, Wang and Leuning, 1998
emissivity_soil = 0.94

# Table 3, Wang and Leuning, 1998
soil_reflectance = 0.1 #(same as MAESTRA)

# light extinction coefficient
k = 0.5

# extinction coefficient of nitrogen in the canopy, assumed to be 0.3 by
# default which comes half Belinda's head and is supported by fig 10 in
# Lloyd et al
#kn = 0.3
kn = 0.001 #DK no extinction of nitrogen through canopy depth

# empirical param related to the leaf angle dist (= 0 for spherical LAD)
chi = 9.99999978E-03

diameter = 3.25 # chamber
footprint = np.pi * (diameter / 2.)**2 # to convert from tree to m2
