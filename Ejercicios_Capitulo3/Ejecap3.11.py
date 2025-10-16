def horner_poly_and_deriv(coeffs, x0):
    """
    Evalúa el polinomio y su derivada en x0 usando la regla de Horner.
    coeffs: lista de coeficientes [a_n, ..., a_0] (grado n a 0)
    x0: punto de evaluación
    Retorna (p(x0), p'(x0))
    """
    n = len(coeffs)
    p = coeffs[0]  # valor del polinomio
    dp = 0         # valor de la derivada
    for i in range(1, n):
        dp = dp * x0 + p
        p = p * x0 + coeffs[i]
    return p, dp

# Ejemplo: p(x) = 2x^3 + 3x^2 + 5x + 7
coeffs = [2, 3, 5, 7]
x0 = 1.5
valor, derivada = horner_poly_and_deriv(coeffs, x0)
print(f"p({x0}) = {valor}")
print(f"p'({x0}) = {derivada}")