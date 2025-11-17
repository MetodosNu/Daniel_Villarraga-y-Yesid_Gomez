"""8.37 [P] Calcule los seis primeros autovalores de la ecuación de Mathieu (para q = 1.5 con n = 150) 
usando una aproximación de mayor orden para la segunda derivada. Es decir, en lugar de la Ec. (8.121), 
que tiene error O(h^2), use una aproximación con error O(h^8)."""

"""
Autovalores de Mathieu usando un O(h^8) de diferencias finitas para d^2/dx^2.

Calcula los primeros 6 autovalores 'a' de:
    -y''(x) + 2 q cos(2x) y(x) = a y(x),
en [0, 2π) con condiciones periódicas.

Parámetros: q = 1.5, n = 150 (número de puntos).
"""

import numpy as np

def build_D2_periodic(n, L):
    """
    Construye la matriz de la segunda derivada (d^2/dx^2) con esquema central
    de orden O(h^8) (stencil de 9 puntos: offsets -4..+4), con condiciones periódicas.
    Devuelve una matriz numpy (n x n).
    """
    h = L / n
    h2 = h * h

    # coeficientes para el stencil 9 puntos (centro c0, desplazamientos c1..c4)
    c0 = -205.0 / 72.0
    c1 = 8.0 / 5.0
    c2 = -1.0 / 5.0
    c3 = 8.0 / 315.0
    c4 = -1.0 / 560.0

    # inicializar matriz d2 (la aproximación da d^2/dx^2 y la dividimos por h^2)
    D2 = np.zeros((n, n), dtype=float)

    # llenar la matriz usando condiciones periódicas (wrap indices modulo n)
    # aportes simétricos: offsets 0, ±1, ±2, ±3, ±4
    for i in range(n):
        # centro
        D2[i, i] = c0 / h2
        # offsets
        D2[i, (i + 1) % n] = c1 / h2
        D2[i, (i - 1) % n] = c1 / h2
        D2[i, (i + 2) % n] = c2 / h2
        D2[i, (i - 2) % n] = c2 / h2
        D2[i, (i + 3) % n] = c3 / h2
        D2[i, (i - 3) % n] = c3 / h2
        D2[i, (i + 4) % n] = c4 / h2
        D2[i, (i - 4) % n] = c4 / h2

    return D2

def compute_mathieu_eigenvalues(q=1.5, n=150, k_eigs=6):
    """
    Construye la matriz A = -D2 + diag(2 q cos(2x)) y devuelve los primeros k_eigs autovalores.
    """
    L = 2.0 * np.pi
    x = np.linspace(0.0, L, n, endpoint=False)
    D2 = build_D2_periodic(n, L)

    # operador A = -d2/dx2 + 2 q cos(2x)
    potential = 2.0 * q * np.cos(2.0 * x)
    A = -D2 + np.diag(potential)

    # autovalores y autovectores (A simétrica real)
    w, v = np.linalg.eigh(A)   # w: autovalores ordenados ascendente
    # tomar los primeros k_eigs (más pequeños)
    first_vals = w[:k_eigs].copy()
    return x, A, w, v, first_vals

if __name__ == "__main__":
    q = 1.5
    n = 1000
    k = 6
    x, A, w, v, first_vals = compute_mathieu_eigenvalues(q=q, n=n, k_eigs=k)

    print(f"q = {q}, n = {n}")
    print(f"Primeros {k} autovalores (a):")
    for i, val in enumerate(first_vals, start=1):
        print(f"  a_{i:1d} = {val:.12f}")