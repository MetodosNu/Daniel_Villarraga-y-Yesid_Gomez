import numpy as np
import matplotlib.pyplot as plt

def grad_forward(phi, x, h=1e-5):
    """
    Calcula el gradiente de phi en el punto x usando diferencias hacia adelante.
    phi: función escalar, recibe un vector x
    x: array/lista con las coordenadas [x0, x1, ...]
    h: paso pequeño
    Retorna: array con las derivadas parciales en cada dirección
    """
    x = np.array(x, dtype=float)
    grad = np.zeros_like(x)
    for i in range(len(x)):
        x_forward = x.copy()
        x_forward[i] += h
        grad[i] = (phi(x_forward) - phi(x)) / h
    return grad

# Ejemplo: phi(x, y) = x^2 + y^2
def phi(x):
    return x[0]**2 + x[1]**2 + x[1]**4

# Puntos para graficar
X = np.linspace(-2, 2, 20)
Y = np.linspace(-2, 2, 20)
XX, YY = np.meshgrid(X, Y)
dphidx = np.zeros_like(XX)
dphidy = np.zeros_like(YY)

for i in range(XX.shape[0]):
    for j in range(XX.shape[1]):
        grad = grad_forward(phi, [XX[i, j], YY[i, j]])
        dphidx[i, j] = grad[0]
        dphidy[i, j] = grad[1]

plt.figure(figsize=(8,6))
plt.quiver(XX, YY, dphidx, dphidy)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gradiente de $\phi(x, y) = x^2 + y^2$')
plt.grid(True)
plt.show()