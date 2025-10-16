



import numpy as np
import matplotlib.pyplot as plt

def f(x):
    # Fórmula original, puede dar problemas numéricos para x muy pequeño
    return (1 - np.cos(x)) / x**2

def f_alt(x):
    # Fórmula alternativa usando una identidad trigonométrica, más precisa para x pequeño
    return 2 * np.sin(x/2)**2 / x**2

# (a) Graficar la función para x pequeño
x = 0.1 * np.arange(1, 101)
y = f(x)

plt.plot(x, y, 'o-')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(r'$f(x) = \frac{1 - \cos x}{x^2}$')
plt.grid(True)
plt.show()

# (b) Límite analítico usando L'Hôpital: f(x) → 0.5 cuando x → 0
print("Valor analítico para x→0:", 0.5)

# (c) Evaluar f(x) para x muy pequeño
x_peq = 1.2e-8
print("f(x_small) =", f(x_peq))  # Puede dar mal resultado por cancelación

# (d) Evaluar la versión alternativa para x muy pequeño
print("f_alt(x_small) =", f_alt(x_peq))  # Resultado mucho más preciso