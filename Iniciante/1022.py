n = int(input())



for _ in range(n):
    linha = input().split()

N1 = int(linha[0])
D1 = int(linha[2])
operador = linha[3]
N2 = int(linha[4])
D2 = int(linha[0])

Soma = (N1 * D2 + N2 * D1) / (D1 * D2)
Subtração = (N1 * D2 - N2 * D1) / (D1 * D2)
Multiplicação = (N1 * N2) / (D1 * D2)
Divisão = (N1 / D1) / (N2 / D2)


