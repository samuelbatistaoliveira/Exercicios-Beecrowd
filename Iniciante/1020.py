N = int(input())

anos = N // 365
dias_restantes = N % 365
meses = dias_restantes // 30
dias = dias_restantes % 30

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")
