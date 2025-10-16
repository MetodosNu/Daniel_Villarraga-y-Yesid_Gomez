from math import sqrt
def f(x,nmax=100):
 for i in range(nmax):
    x = sqrt(x)
 for i in range(nmax):
    x = x**2
 return x

for xin in (5., 5e100):
 xout = f(xin); print(xin, xout)

"""Lo que pasa en el código es que al hacer muchas veces la raiz cuadrada de un número 
ese valor se va acercando a 1 para números mayores que 1 y a 0 para números así 0<x<1
y al llevar el error de la operación muchas veces el resultado se estanca en 1 o 0
y luego al elevar ese 1 al cuadrado muchas veces el resultado sigue siendo 1"""
