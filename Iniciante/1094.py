n = int(input())

coelho = 0 
sapo = 0 
rato = 0

for i in range(n):
    quantidade, tipo = input().split()
    quantidade = int(quantidade)

    if tipo == "C":
        coelho += quantidade
    elif tipo == "R":
        rato += quantidade
    elif tipo == "S":
         sapo += quantidade


total = coelho + rato + sapo
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelho}")
print(f"Total de ratos: {rato}") 
print(f"Total de sapos: {sapo}")


percentual_coelho = (coelho / total) * 100
percentual_rato = (rato/total) * 100
percentual_sapo = (sapo/total) * 100
print(f"Percentual de coelhos: {percentual_coelho:.2f} %")
print(f"Percentual de ratos: {percentual_rato:.2f} %")
print(f"Percentual de sapos: {percentual_sapo:.2f} %")