horainicial,minutoinicial,horafinal,minutofinal = map(int,input().split())

min_Inicio = (horainicial * 60) + minutoinicial
min_fim = (horafinal * 60) + minutofinal
duracao_minutos = min_fim - min_Inicio

if duracao_minutos <= 0:
    duracao_minutos += 1440

horas = duracao_minutos // 60
minutos = duracao_minutos % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")