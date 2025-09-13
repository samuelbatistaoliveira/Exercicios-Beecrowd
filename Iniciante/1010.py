codigo1, peca1, valor1 = input().split()
codigo2, peca2, valor2 = input().split()

total = (int(peca1) * float(valor1)) + (int(peca2) * float(valor2))
print(f'VALOR A PAGAR: R$ {total:.2f}')