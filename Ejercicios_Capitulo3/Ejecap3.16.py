import numpy as np

def g(n):
    """Perímetro del polígono inscrito con 2^n lados en círculo de diámetro 1."""
    return 2**n * np.sin(np.pi / 2**n)

# (a) Expansión de Taylor (comentario):
# sin(pi/2^n) ≈ pi/2^n - (pi/2^n)^3/6 + ... así que g_n ≈ pi - pi^3/(3*2^{2n}) + ...

# (b) Richardson extrapolation
n_vals = np.arange(2, 11)
g_vals = np.array([g(n) for n in n_vals])

# h = 2^{-n}
h_vals = 2.0**(-n_vals)

# Extrapolacion de Richardson: G = (4g(h/2) - g(h))/3
# g(h/2) corresponde a n+1, g(h) a n
G_vals = (4 * g_vals[1:] - g_vals[:-1]) / 3

print("n\tg_n\t\tG_n (Richardson)")
for i in range(len(G_vals)):
    print(f"{n_vals[i]:2d}\t{g_vals[i]:.20f}\t{G_vals[i]:.20f}")

# (c) Segunda ronda de Richardson extrapolation (p=4, q=2)
# G(h) y G(h/2): G_vals[:-1] y G_vals[1:]
G2_vals = (16 * G_vals[1:] - G_vals[:-1]) / 15

print("\nn\tG2_n (Richardson 2)")
for i in range(len(G2_vals)):
    print(f"{n_vals[i]:2d}\t{G2_vals[i]:.20f}")

# Valor real de pi
print(f"\nValor real de pi: {np.pi:.20f}")