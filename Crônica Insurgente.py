import time
time.sleep(2)

import random


#===========================

#       APRESENTAÇÃO

#===========================



print("---------[CRÔNICA INSURGENTE]---------")

print("Bem vindo viajante")
print("Nesse projeto, você jogará como o transcedente")
print("Usando sua vontade(a vontade do personagem é representada por um palavra) para lutar contra a do Imortal")
print("OBS:Esse é um jogo de combate por turnos")

input("Aperte enter para continuar: ")

print("Sipnose:\nUm mundo devastado pela miséria e discordia")
print("Nem sempre foi assim, tudo era colorido e abundante de vida.\nmas os, humanos, eles tinham uma ganância sem fim.")
print("Durante uma das várias extrações de recursos naturais deles,\ndespertaram o Imortal - antigo guardião da natureza, adormecido")
print("E o trancendente, aquele que foi criado só para impedir que a humanidade seja exterminada")

input("\nAperte enter para continuar: ")


#===========================

#     DICIONÁRIO DE VONTADES

#===========================



jogador = {
    "nome": "Rebelião",
    "vida_atual": 95,
    "vida_máxima": 95,
    "poções": 2,
    "ataques": ("expurgo", "rebeliao")
}

inimigo = {
    "nome": "Divindade",
    "vida_atual": 100,
    "vida_máxima": 100,
    "poções": 1,
    "ataques": ("romper", "distorcao")
}



#   =====================

#   DICIONÁRIO DE ATAQUES

#   ======================

ataques = {

    "rebeliao": {
        "tipo": "multi dano",
        "golpes": 5,
        "dano": 5
    },

    "expurgo": {
        "tipo": "dano contínuo",
        "duração": 3,
        "dano": 15
    },

    "romper": {
        "tipo": "normal",
        "dano": 10
    },

    "distorcao": {
        "tipo": "normal",
        "dano": 15
    }
}



#========================


#    DICIONÁRIO DE POÇÕES


#=======================


pocoes = {
    "pocao pequena": {
        "cura": 20
    },

    "pocao grande": {
        "cura": 40
    }
}


#==================


#FLUXO DA PARTIDA


#===================

#---STATUS INICIAL---


print(
    f"\n{jogador['nome']} -> "
    f"{jogador['vida_atual']} HP"
)

print(
    f"{inimigo['nome']} -> "
    f"{inimigo['vida_atual']} HP"
)


#---INÍCIO DO COMBATE---


primeiro_turno = random.choice([
    jogador["nome"],
    inimigo["nome"]
])

print(f"\nO {primeiro_turno} atacará primeiro")

# variável do efeito persistente
efeito_persistente = {

    "ativo": False,

    "dano": 0,

    "duracao": 0
}

turno = 0

#==========================================
#             LAÇO PRINCIPAL
# ==========================================

# continua enquanto os dois estiverem vivos
while (
    jogador["vida_atual"] > 0
    and inimigo["vida_atual"] > 0
):

    turno += 1

    print(f"\n========== TURNO {turno} ==========")

    # ==========================================
    #           TURNO DO JOGADOR
    # ==========================================

    print("\nO que deseja fazer?")
    print("1 - Atacar")
    print("2 - Usar Poção")

    acao = int(input("\nEscolha: "))

    # ==========================================
    #                ATACAR
    # ==========================================

    if acao == 1:

        print("\nEscolha um ataque:")

        # mostra os ataques do jogador
        for indice, ataque in enumerate(
            jogador["ataques"],
            start=1
        ):

          print(f"{indice} - {ataque}")

        escolha_ataque = int(
            input("\nDigite o número: ")
        )

# verifica se escolheu um ataque válido
        if (
            1 <= escolha_ataque
            <= len(jogador["ataques"])
        ):

            # pega o nome do ataque
            ataque_escolhido = (
                jogador["ataques"][
                    escolha_ataque - 1
                ]
            )

# pega os dados do ataque
            
dados_ataque = ataques[ataque_escolhido]

print(f"\n{jogador['nome']} usou {ataque_escolhido}!")

if dados_ataque["tipo"] == "multi dano":

    golpes = random.randint(1, dados_ataque["golpes"])

    dano_total = golpes * dados_ataque["dano"]

    inimigo["vida_atual"] -= dano_total

    print(f"Foram {golpes} golpes!")
    print(f"Causou {dano_total} de dano!")

elif dados_ataque["tipo"] == "dano contínuo":

    efeito_persistente["ativo"] = True
    efeito_persistente["dano"] = dados_ataque["dano"]
    efeito_persistente["duracao"] = dados_ataque["duração"]

    print("O inimigo foi afetado por dano contínuo!")
            

























