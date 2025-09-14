import math

line = input()
A,B,C = map(float, line.split())
pi = 3.14159

trianguloretangulo = (A * C) / 2
areadocirculo = pi * math.pow(C,2)
areadotrapezio = (A + B) * C / 2
areadoquadrado = B * B
areadoretangulo = A * B

print(f"TRIANGULO: {trianguloretangulo:.3f}")
print(f"CIRCULO: {areadocirculo:.3f}")
print(f"TRAPEZIO: {areadotrapezio:.3f}")
print(f"QUADRADO: {areadoquadrado:.3f}")
print(f"RETANGULO: {areadoretangulo:.3f}")