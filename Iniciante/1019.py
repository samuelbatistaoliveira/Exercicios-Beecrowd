valor = int(input())

Horas = valor // 3600
Minutos = (valor % 3600) // 60
Segundos = (valor % 3600) % 60

print(f"{Horas}:{Minutos}:{Segundos}")