"""
Se pide usar la serie de Taylor para aproximar la función sin(x) en 0.1 y 40
"""

import math

def taylor_sin(x, nmax=30):
    suma = 0.0
    term = x  # primer término (n=0)
    suma += term
    for n in range(1, nmax):
        term *= -x**2 / ((2*n)*(2*n+1))
        suma += term
    return suma

# Evaluar en x = 0.1 y x = 40
for x in [0.1, 40]:
    approx = taylor_sin(x)
    real = math.sin(x)
    print(f"x = {x}")
    print(f"Serie de Taylor: {approx}")
    print(f"math.sin(x):    {real}")
    print(f"Error absoluto: {abs(approx-real)}\n")

# sin(x) = sin(x - 2*pi*k), donde k es un entero tal que x-2*pi*k está en [-pi, pi]
x_large = 40
x_reduced = ((x_large + math.pi) % (2*math.pi)) - math.pi  # Lleva x a [-pi, pi]
approx_reduced = taylor_sin(x_reduced)
real_large = math.sin(x_large)
print(f"x reducido = {x_reduced}")
print(f"Serie de Taylor en x reducido: {approx_reduced}")
print(f"math.sin({x_large}): {real_large}")
print(f"Error absoluto usando x reducido: {abs(approx_reduced-real_large)}")