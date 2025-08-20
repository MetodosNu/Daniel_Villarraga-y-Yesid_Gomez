import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import matplotlib.cm as cm

"""
4 [P] Estudiar isotermas de metano con la ecuación de estado de van der Waals.

(a) Grafique 40 isotermas (es decir, curvas de T constante, mostrando P vs v), donde T va de 162 a 210 K, v va de 1.5b a 9b y las curvas se
 vean suaves.

(b) Si resolvió correctamente la parte anterior, apenas debería poder distinguir las diferentes curvas. Embellezca su gráfico empleando 
un mapa de colores automático.
"""
"""
Constantes físicas 
R = J / (mol*K)
a = (Pa*m^6) / mol^2
b = m^3 / mol
"""
R = 8.314462618  
a = 0.2283       
b = 4.287e-5     
h = 1e-6

# Ecuación de Van der Waals
def P_vdw(v, T):
    return R * T / (v - b) - a / (v**2)

# metodo de diferencia central
def dP_dv_central(v, T, h):
    return (P_vdw(v + h/2, T) - P_vdw(v - h/2, T)) / (h)

# metodo de Richardson
def dP_dv_richardson(v, T, h):
    D_h = dP_dv_central(v, T, h)
    D_h2 = dP_dv_central(v, T, h/2)
    return (4*D_h2 - D_h) / 3

# Reconstrucción de P(v) usando derivadas aproximadas
def aproximar_isoterma(T, v_vals, metodo="central", h = h):
    P_vals = [P_vdw(v_vals[0], T)]  # condición inicial
    for i in range(1, len(v_vals)):
        v = v_vals[i-1]
        if metodo == "central":
            dP = dP_dv_central(v, T, h)
        elif metodo == "richardson":
            dP = dP_dv_richardson(v, T, h)
        else:
            raise ValueError("Método no reconocido")

        delta_v = v_vals[i] - v_vals[i-1]
        P_vals.append(P_vals[i-1] + dP*delta_v)
    return P_vals

# ---- Graficar isotermas con métodos numéricos ----
def graficar_isotermas_aprox(metodo="central"):
    T_min, T_max = 162, 210
    n_isotermas = 40
    T_vals = np.linspace(T_min, T_max, n_isotermas)

    v_min, v_max = 1.5*b, 9*b
    n_v = 200
    v_vals = np.linspace(v_min, v_max, n_v)

    # Colormap
    cmap = cm.viridis
    norm = Normalize(vmin=T_min, vmax=T_max)

    plt.figure(figsize=(16,9))
    for T in T_vals:
        color = cmap(norm(T))
        P_vals = aproximar_isoterma(T, v_vals, metodo=metodo)
        plt.plot(v_vals/b, np.array(P_vals)/1e5, color=color, linewidth=1.2)

    plt.xlabel("v/b")
    plt.ylabel("P (bar)")
    plt.title(f"isotermas de Metano (Método: {metodo})")
    plt.grid(True)

    # Barra de colores
    sm = cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    ax = plt.gca()
    plt.colorbar(sm, ax=ax, label="Temperatura (K)")

    plt.show()

# ---- Ejecutar con método deseado ----
graficar_isotermas_aprox(metodo="central")      # isotermas con diferencia central
graficar_isotermas_aprox(metodo="richardson")  # isotermas con Richardson
