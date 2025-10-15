animais = {
    "vertebrado" : {
        "ave" : {
            "carnivoro": "aguia",
            "onivoro": "pomba"
        },
        "mamifero": {
            "onivoro" : "homem",
            "herbivoro" : "vaca"
        }
    },
    "invertebrado" : {
        "inseto" : {
            "hematofago" :"pulga",
            "herbivoro" : "lagarta"
        },
        "anelideo" : {
            "hematofago" : "sanguessuga",
            "onivoro" : "minhoca"
        },
    }
}

c1 = input()
c2 = input()
c3 = input()

print(animais[c1][c2][c3])