import math
from math import pi, sqrt
import cmath

L = 2  # lado de la caja
cardinal = 0  # cardinales de 0 a 999
posicion = [1,1,1]  # posición (x,y,z)

def cardinal_a_triple(cardinal, nmax=10):
    """Devuelve la terna (nx, ny, nz) correspondiente al número cardinal."""
    if cardinal < 0:
        raise ValueError("El cardinal debe ser un entero no negativo.")
    triples = []
    for nx in range(1, nmax+1):
        for ny in range(1, nmax+1):
            for nz in range(1, nmax+1):
                triples.append((nx, ny, nz))
    # Ordenar por nx^2 + ny^2 + nz^2
    triples.sort(key=lambda t: t[0]**2 + t[1]**2 + t[2]**2)
    return triples[cardinal]

def vectorO(cardinal,L):
    """Devuelve el vector de onda (kx, ky, kz) para el número cardinal."""
    nx, ny, nz = cardinal_a_triple(cardinal)

    return (2*pi*nx/L, 2*pi*ny/L, 2*pi*nz/L)

def psibox3D(cardinal, L):
    """Función de onda tipo 1/sqrt{L^3} * e^{i k·r} ."""
    kx, ky, kz = vectorO(cardinal, L)
    norm = 1 / (sqrt(L**3))
    x, y, z = posicion
    phase = kx*x + ky*y + kz*z 
    psi = norm * cmath.exp(1j * phase)
    return psi

print(f"Terna del cardinal {cardinal}: (nx, ny, nz):", cardinal_a_triple(cardinal))
print("Vector de onda (kx, ky, kz):", vectorO(cardinal, L))
print("Valor de la función de onda:", psibox3D(cardinal, L))