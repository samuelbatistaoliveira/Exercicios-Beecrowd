valor = float(input())
valor = int(round(valor * 100))

notas = (10000, 5000, 2000, 1000, 500, 200)
moedas = (100, 50, 25, 10, 5, 1)

print("NOTAS:")
for n in notas:
    qtd = valor // n
    print(f"{qtd} nota(s) de R$ {n/100:.2f}")
    valor %= n

print("MOEDAS:")
for m in moedas:
    qtd = valor // m
    print(f"{qtd} moeda(s) de R$ {m/100:.2f}")
    valor %= m
