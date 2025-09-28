valor_total = int(input())
print(valor_total)


cedulas = [100, 50, 20, 10, 5, 2,1]

valor_atual = valor_total

for cedula in cedulas:
    quantidade_notas = valor_atual // cedula
    valor_atual = valor_atual % cedula
    print(f"{quantidade_notas} nota(s) de R$ {cedula},00")