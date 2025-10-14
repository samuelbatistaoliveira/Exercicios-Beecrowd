horainicial, horafinal = map(int,input().split())

if horafinal > horainicial:
    duraçao = horafinal - horainicial
else:
    duraçao = (24 - horainicial) + horafinal

print(f"O JOGO DUROU {duraçao} HORA(S)")