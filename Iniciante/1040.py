notas = list(map(float, input().split()))

pesos = [2,3,4,1]

media = sum(notas[i] * pesos [i] for i in range(4)) / sum(pesos)

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input())
    medialfinal = (nota_exame + media) / 2
    print(f"Nota do exame: {nota_exame:.1f}")
    if medialfinal >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {medialfinal:.1f}")