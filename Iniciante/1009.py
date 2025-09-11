nome = str(input())
salariofixo = float(input())
totalvendas = float(input())

comissao = totalvendas * 0.15
salariototal = salariofixo + comissao
print(f"TOTAL = R$ {salariototal:.2f}")