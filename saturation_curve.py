import numpy as np
from matplotlib import pyplot as plt
from CoolProp.CoolProp import PropsSI

# Définition du fluide
fluid = "water"

# Propriétés critiques et limites
T_crit = PropsSI("Tcrit", fluid)
p_crit = PropsSI("pcrit", fluid)
s_crit = PropsSI("S", "T", T_crit, "P", p_crit, fluid)
s_triple1 = PropsSI("S", "T", 273.16, "Q", 0, fluid)
s_triple2 = PropsSI("S", "T", 273.16, "Q", 1, fluid)

t_min = PropsSI("T", "P", 611.655, "Q", 0, fluid)
temperatures = np.arange(t_min, T_crit, 0.1)

# Calcul des courbes de saturation
entropie_liquide = PropsSI("S", "T", temperatures, "Q", 0, fluid)
entropie_vapeur = PropsSI("S", "T", temperatures, "Q", 1, fluid)

# Tracé du diagramme T-s
plt.figure(figsize=(8, 6))
plt.plot(entropie_liquide / 1000, temperatures - 273.15, label="Saturation (liquide)", color="blue")
plt.plot(entropie_vapeur / 1000, temperatures - 273.15, label="Saturation (vapeur)", color="red")

plt.xlabel("Entropie (kJ/kg/K)")
plt.ylabel("Température (°C)")
plt.title("Diagramme T-s de la cloche de saturation de l'eau")

# Ajout des points clés
plt.plot(s_crit / 1000, T_crit - 273.15, marker="x", markersize=10, markeredgecolor="black", label="Point critique")
plt.plot(s_triple1 / 1000, 0.01, marker="o", markersize=10, color="k", label="Point triple")
plt.plot(s_triple2 / 1000, 0.01, marker="o", markersize=10, color="k")

plt.legend()
plt.grid()
plt.show()