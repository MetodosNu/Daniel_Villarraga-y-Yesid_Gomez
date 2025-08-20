import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parte A) Calcular el polinomio de Legendre asociado a Bonnet
"""
# Calcula Pnm(x) aplicando paso a paso la Ec. (2.125), utilizando las Ecs. (2.126) y (2.127) cuando sea necesario.
#Usa tu función para graficar 𝑃42(𝑥)P42(x).
"""
m = 2    # Orden del polinomio
n = 4   # Potencia del polinomio

def doble_factorial(n):
    """
    Calcula el doble factorial de un número entero, si el número es negativo devuelve 1
    """
    if n <= 0:
        return 1
    result = 1
    for k in range(n, 0, -2):
        result *= k
    return result

def Polinomio_asociado(n, m, x):
    """
    Calcula el polinomio de legendre asosciado a la relación de recurrencia de Bonnet
    n: grado (entero > 0)
    m: orden (entero entre n y -n)
    """
# Verificamos primero que m sea menor que n

    if  abs(m) > n:
        raise ValueError("Debe cumplirse |m| <= n")
    
# Si m es menor que 0 usamos la expresión (2.128):
    
    elif m < 0:
        return ((-1)**m) * math.factorial(n - abs(m)) / math.factorial(n + abs(m)) * Polinomio_asociado(n, abs(m),x)
    
# El caso base recomendado 2.126 n=m, aquí aplicamos la función doble_factorial:

    elif m == n:
        return (-1)**m * doble_factorial(2*m-1) * (1-x**2)**(m/2)

# Ahora para el caso 2.127 n=m+1:

    elif n == m+1:
         return x * (2*m + 1) * Polinomio_asociado(m, m, x)
    
# Luego, para el caso general donde 0 < m < n  se tiene:
    return ((x * (2*n - 1) * Polinomio_asociado(n-1, m, x)) - ((n + m - 1) * Polinomio_asociado(n-2, m, x))) / (n - m)

#Gráfica del Polinomio

x_vals = np.linspace(-1, 1, 300)
P = [Polinomio_asociado(n, m, x) for x in x_vals]
plt.plot(x_vals, P, label=f"$P_n^m(x)$")
plt.legend()
plt.xlabel("x")
plt.ylabel("P(x)")
plt.title("Polinomios de Legendre asociados")
plt.grid(True)
plt.show()

# Parte B) Crear una función Y que calcule los armonicos reales esfericos
def Y(n, m, theta, phi):
    """
    Calcula el armonico esférico real "Y"
    n: grado (entero > 0)
    m: orden (entero entre n y -n)
    theta: ángulo (entre 0 y pi)
    phi: ángulo (entre 0 y 2pi)
    """
    # igual que en la función anterior, verificamos que m esté entre n y -n
    if  abs(m) > n:
        raise ValueError("Debe cumplirse |m| <= n")
    
    #aplicamos el caso para m < 0

    if m < 0:
        coef = (-1)**m * np.sqrt(2) * np.sqrt((2*n+1)/(4*math.pi) * math.factorial(n-abs(m))/math.factorial(n+abs(m)))
        return coef * Polinomio_asociado(n, abs(m), np.cos(theta)) * np.sin(abs(m)*phi)
    
    # el caso para m=0

    elif m == 0:
        coef = np.sqrt((2*n+1)/(4*math.pi))
        return coef * Polinomio_asociado(n, 0, np.cos(theta))
    
    # y el caso para m > 0

    else: # m > 0
        coef = (-1)**m * np.sqrt(2) * np.sqrt((2*n+1)/(4*np.pi) * 
                                                  math.factorial(n-m)/math.factorial(n+m))
        return coef * Polinomio_asociado(n, m, np.cos(theta)) * np.cos(m*phi)
    
# Parte C) Crear una malla para graficar Y
"""
(c) Genera una malla para Theta de 0 a pi y de phi a 2pi. Visualiza ∣𝑌42∣ usando un gráfico polar 3D, lo cual está disponible en Axes3D.plot_surface().
De manera similar a vectorfield.py, debes usar listas anidadas para producir las cantidades relevantes y finalmente convertirlas a arreglos de NumPy.
Nuestro problema es tridimensional en coordenadas cartesianas, así que deberás pasar como argumentos las formas convertidas apropiadamente de ∣Y42|
"""

# Se crea malla de theta y phi para hacer la gráfica de Y
theta = np.linspace(0, np.pi, 150)   
phi = np.linspace(0, 2*np.pi, 150)   
theta, phi = np.meshgrid(theta, phi)

# Se calcula |Y_nm(theta, phi)|
Ynm = np.vectorize(lambda th, ph: Y(n, m, th, ph))(theta, phi)
R = np.abs(Ynm)  # valor absoluto

# Convertir a coordenadas cartesianas
X = R * np.sin(theta) * np.cos(phi)
Yc = R * np.sin(theta) * np.sin(phi)
Z = R * np.cos(theta)

# Se hace la gráfica Ynm
fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Yc, Z, cmap="viridis", edgecolor="none")

ax.set_title("Visualización en 3D de $|Y_n^m(θ, φ)|$")
fig.colorbar(surf, shrink=0.5, aspect=10, label="$|Y_n^m|$")
plt.show()
