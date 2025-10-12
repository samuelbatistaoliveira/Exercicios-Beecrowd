valores = list(map(int,input().split()))
valores_ordenados = valores[:]
valores_ordenados.sort()

for valor in valores_ordenados:
    print(valor)

print()

for valor in valores:
    print(valor)