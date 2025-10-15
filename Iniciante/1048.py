salario = float(input())

percentual_int = 0.0

if salario >= 0 and salario <= 400.00:
    percentual_int = 0.15
elif salario >= 400.01 and salario <= 800.00:
    percentual_int = 0.12    
elif salario >= 800.01 and salario <= 1200.00:
    percentual_int = 0.10
elif salario >= 1200.01 and salario <= 2000.00:
    percentual_int = 0.07
else:
    percentual_int = 0.04

reajuste_ganho = salario * percentual_int
novo_salario = salario + reajuste_ganho
percentual_int = round(percentual_int * 100) 


print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste_ganho:.2f}")
print(f"Em percentual: {percentual_int} %")