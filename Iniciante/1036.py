import math

a, b, c, = map(float, input().split())

delta = math.pow(b,2) - (4 * a * c)

if a == 0 or delta < 0:
    print("Impossivel calcular")
else:
    raiz_delta = math.sqrt(delta)
    R1 = (-b + raiz_delta) / (2 * a)
    R2= (-b - raiz_delta) / (2 * a)
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")
