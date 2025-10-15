destinos = {
    61 : "Brasilia",
    71 : "Salvador",
    11 : "Sao Paulo",
    21 : "Rio de Janeiro",
    32 : "Juiz de Fora",
    19 : "Campinas",
    27 : "Vitoria",
    31 : "belo Horizonte"
}
ddd = int(input())
resultado = destinos.get(ddd, "DDD nao cadastrado")
print(resultado)