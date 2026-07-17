import random


# ==========================================
#          SISTEMA DE ATAQUE CRÍTICO
# ==========================================

def aplicar_critico(dano, chance):

    sorte = random.randint(1, 100)

    if sorte <= chance:

        print("\n💥 GOLPE CRÍTICO!")

        dano_final = dano * 2

        return dano_final


    return dano



# ==========================================
#          CAUSAR DANO SEGURO
# ==========================================

def causar_dano(alvo, dano):

    alvo["vida_atual"] -= dano


    if alvo["vida_atual"] < 0:

        alvo["vida_atual"] = 0



# ==========================================
#              CURAR PERSONAGEM
# ==========================================

def curar(personagem, quantidade):

    vida_antiga = personagem["vida_atual"]


    personagem["vida_atual"] += quantidade


    if personagem["vida_atual"] > personagem["vida_maxima"]:

        personagem["vida_atual"] = personagem["vida_maxima"]


    return personagem["vida_atual"] - vida_antiga

# ==========================================
#          SISTEMA DE DEFESA
# ==========================================

def ativar_defesa(personagem):

    personagem["defesa"] = True

    print(
        f"\n🛡 {personagem['nome']} "
        "entrou em posição defensiva!"
    )



def aplicar_defesa(personagem, dano):

    if personagem["defesa"]:

        dano_reduzido = dano // 2

        print(
            "\n🛡 A defesa reduziu "
            "metade do dano!"
        )

        personagem["defesa"] = False

        return dano_reduzido


    return dano