"""
Solucion al ejercicio 2.7 del libro, en el punto b se observa un resultado erroneo ya que se usan
flotantes y ocurre una cancelacion catastrófica, en el punto c se usa la diferencia de cuadrados
para evitar ese problema y se obtiene el resultado correcto.
"""

# (a) Cálculo exacto con enteros
x_ent = 1234567891234567
y_ent = 1234567891234566
exacto = x_ent**2 - y_ent**2
print("Cálculo exacto con enteros:", exacto)

# (b) Cálculo con flotantes (puede haber cancelación catastrófica)
x_float = 1234567891234567.0
y_float = 1234567891234566.0
flotante = x_float**2 - y_float**2
print("Cálculo con flotantes:", flotante)

# (c) Diferencia de cuadrados con flotantes
Dc = (x_float - y_float) * (x_float + y_float)
print("Diferencia de cuadrados con flotantes:", Dc)

