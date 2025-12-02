maior = int(input())
posicao = 1


for i in range(2,101):
    n = int(input())
    if n > maior:
        maior = n
        posicao = i


print(maior)
print(posicao)