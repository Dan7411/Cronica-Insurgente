import random


def aplicar_critico(dano, chance):

    if random.randint(1,100) <= chance:

        print("\n💥 GOLPE CRÍTICO!")

        return dano * 2

    return dano



def aplicar_defesa(personagem, dano):

    if personagem["defesa"]:

        dano = dano // 2

        print(
            "\n🛡 Defesa reduziu o dano!"
        )

        personagem["defesa"] = False

    return dano



def causar_dano(alvo, dano):

    alvo["vida_atual"] -= dano

    if alvo["vida_atual"] < 0:

        alvo["vida_atual"] = 0

    return dano

def curar(personagem, valor):

    antes = personagem["vida_atual"]

    personagem["vida_atual"] += valor


    if personagem["vida_atual"] > personagem["vida_maxima"]:

        personagem["vida_atual"] = personagem["vida_maxima"]


    return personagem["vida_atual"] - antes

# ==========================
# ATIVAR DEFESA
# ==========================

def ativar_defesa(personagem):

    personagem["defesa"] = True

    print(f"\n🛡 {personagem['nome']} entrou em posição defensiva!")