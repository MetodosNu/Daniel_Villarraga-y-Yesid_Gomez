import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(np.sin(2*x))

def df_analitica(x):
    return 2 * np.exp(np.sin(2*x)) * np.cos(2*x)

# Tabla de valores
x = np.arange(0, 1.6 + 0.08, 0.08)
y = f(x)

h = 0.08

# Derivada por diferencia hacia adelante
df_fd = (f(x + h) - f(x)) / h
# Derivada por diferencia central
df_cd = (f(x + h) - f(x - h)) / (2*h)
# Derivada analítica
df_exact = df_analitica(x)

# Extrapolación de Richardson para diferencia hacia adelante
df_fd_2h = (f(x + 2*h) - f(x)) / (2*h)
df_richardson = 2*df_fd - df_fd_2h

# Para graficar, recorta los arrays para evitar índices fuera de rango
x_fd = x[:-1]
df_fd_plot = df_fd[:-1]
df_richardson_plot = df_richardson[:-1]

x_cd = x[1:-1]
df_cd_plot = df_cd[1:-1]

plt.figure(figsize=(8,5))
plt.plot(x, df_exact, 'k-', label='Derivada analítica')
plt.plot(x_fd, df_fd_plot, 'bo', label='Diferencia hacia adelante')
plt.plot(x_cd, df_cd_plot, 'ro', label='Diferencia central')
plt.plot(x_fd, df_richardson_plot, 'gs', label='Richardson extrapolación')
plt.xlabel('$x$')
plt.ylabel('Derivada de $e^{\sin(2x)}$')
plt.title('Aproximaciones numéricas vs derivada analítica')
plt.legend()
plt.grid(True)
plt.show()