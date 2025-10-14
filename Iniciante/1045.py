lados = list(map(float, input().split()))

lados.sort(reverse=True)
A = lados[0]
B = lados[1]
C = lados[2]

if  A >= B + C:
    print("NAO FORMA TRIANGULO")
elif A **2 == B ** 2 + C ** 2:
    print("TRIANGULO RETANGULO")
elif A ** 2 > B ** 2 + C ** 2:
    print("TRIANGULO OBTUSANGULO")
elif A ** 2 < B ** 2 + C ** 2:
    print("TRIANGULO ACUTANGULO")

if A == B == C:
    print("TRIANGULO EQUILATERO")
elif A == B or B == C or A == C:
    print("TRIANGULO ISOSCELES")