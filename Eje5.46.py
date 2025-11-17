"""
5.46)  Volvemos al metano mediante la ecuación de estado de van der Waals, Eq. (5.2); tome T = 170 K. 
Primero, grafique la isoterma (es decir, P frente a v). Luego, para P = 30 atm encuentre los tres valores 
posibles de v. Finalmente, encuentre la presión mínima y el correspondiente v.

Eq. (5.2)  (P+a/v^2)(v-b)=RT
"""
import numpy as np
import matplotlib.pyplot as plt

R=0.08206  # L·atm/(K·mol)
T=170.0    # K  

#Para el metano a y b son:
a=2.253    # L²·atm/mol²
b=0.04278  # L/mol

def Waals(P, V):
    return (P + a / V**2) * (V - b) - R * T

def Presión(V):
    return (R * T) / (V - b) - a / V**2

#para evitar que V=b:
V = np.linspace(b + 0.01, 4.0, 2000)

P_vals= Presión(V)

# Para P = 30 atm: resolver el polinomio cúbico
P_pedido = 30.0
# Coeficientes del cúbico: P v^3 - (P b + R T) v^2 + a v - a b = 0
coeffs = [P_pedido, -(P_pedido * b + R * T), a, -a * b]
roots = np.roots(coeffs)

# filtrar raíces reales (tolerancia) y físicas (v > b)
real_roots = []
for r in roots:
    if np.isclose(r.imag, 0, atol=1e-6):   #Si l la parte imaginaria es cercana a 0 toma solo la parte real
        rv = float(r.real)
        if rv > b:
            real_roots.append(rv)       #Si la raíz real es mayor que b, se considera física y se añade a la lista

# Encontrar extremos (derivada = 0). Usamos forma algebraica:
# RT v^3 - 2a v^2 + 4ab v - 2a b^2 = 0  (derivada igual a cero)
coeffs_ext = [R * T, -2 * a, 4 * a * b, -2 * a * b**2]     #Polinomio con la derivada igual a cero
ext_roots = np.roots(coeffs_ext)        #Se sacan las raices del polinomio para hallar los puntos críticos

ext_real = []
for er in ext_roots:
    if np.isclose(er.imag, 0, atol=1e-8):
        ev = float(er.real)
        if ev > b:
            ext_real.append(ev)  # De igual forma se clasifica y transforma la raiz

# Determinar cuál es mínimo: segunda derivada d2P/dv2 = 2RT/(v-b)^3 - 6a/v^4
min_candidates = []
for ev in ext_real:
    d2 = 2 * R * T / (ev - b)**3 - 6 * a / ev**4    #Segunda derivada evaluada en el extremo
    P_at_ev = Presión(ev)               #Presión en el extremo
    min_candidates.append((ev, P_at_ev, d2))    # lista de tuplas (v_extremo, P_extremo, d2P/dv2)

# seleccionar el extremo con d2>0 (mínimo). Si hay varios, elegir el de menor P.
min_points = [c for c in min_candidates if c[2] > 0]     #crea una tupla que filtra los puntos con d2>0

"""Si no hay mínimos (d2>0), elegir el mínimo P entre los candidatos."""
if len(min_points) == 0:
      #fallback: elegir el mínimo P entre candidatos
    chosen = min(min_candidates, key=lambda x: x[1])
else:
    chosen = min(min_points, key=lambda x: x[1])
v_min, P_min, d2val = chosen

max_points = [c for c in min_candidates if c[2] < 0]    #puntos con d2<0 (máximos)
if len(max_points) > 0:
    chosen_max = max(max_points, key=lambda x: x[1])
v_max, P_max, d2max = chosen_max


# marcar mínimo en la gráfica
# Gráfica de la isoterma

plt.figure(figsize=(7,5))
plt.plot(V, P_vals, label=f'T = {T} K')
plt.ylim(10, 40)  # ajustar visualización
plt.xlim(b, 1.5)
plt.xlabel('v (L/mol)')
plt.ylabel('P (atm)')
plt.title('Isoterma de van der Waals para metano, T=170 K')
plt.plot(v_min, P_min, 'X', markersize=10, label=f'Mínimo: v={v_min:.6f}, P={P_min:.6f} atm')
# marca las raíces en la gráfica
for i, rv in enumerate(real_roots):
    plt.plot(rv, P_pedido, 'bo')
    if i == 1:
        plt.annotate(f'v={rv:.4f} L/mol',
                     xy=(rv, P_pedido), xytext=(rv , P_pedido - 5),   # posición distinta solo para esta
                     arrowprops=dict(arrowstyle='->', color='0.3'))
    else:
        plt.annotate(f'v={rv:.4f}',
                     xy=(rv, P_pedido),
                     xytext=(rv, P_pedido + 5), 
                     arrowprops=dict(arrowstyle='->', color='0.3'))  # posición por defecto para las demás
plt.plot(v_max, P_max, 'o', markersize=8, label=f'Máximo: v={v_max:.6f}, P={P_max:.6f} atm') # Si se quiere marcar el máximo también lo pone
plt.legend()
plt.grid(True)
plt.show()

# Imprimir resultados
print("Raíces (reales y físicas) para P = 30 atm:")
for i, rv in enumerate(real_roots, 1):
    print(f"  v_{i} = {rv:.6f} L/mol")

print(f"\nExtremos (reales y > b):")
for ev, P_ev, d2 in min_candidates:
    kind = "mínimo" if d2 > 0 else "máximo"
    print(f"  v = {ev:.6f} L/mol, P = {P_ev:.6f} atm, d2P/dv2 = {d2:.6e} ({kind})")

print(f"\nPresión mínima encontrada: P_min = {P_min:.6f} atm a v = {v_min:.6f} L/mol")