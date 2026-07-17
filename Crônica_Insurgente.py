import random
import time

from funcoes.historia import (
    mostrar_menu_inicio,
    mostrar_introducao,
    mostrar_sinopse
)

from funcoes.jogador import (
    turno_jogador
)

from funcoes.inimigo import (
    turno_inimigo
)

from funcoes.interface import (
    mostrar_status
)

# ==========================
# HISTÓRIA
# ==========================

escolha_inicio = mostrar_menu_inicio()

if escolha_inicio == "1":

    mostrar_introducao()

    mostrar_sinopse()

elif escolha_inicio == "2":

    mostrar_sinopse()

else:

    print("\n⏩ Pulando para a batalha...")

# ==========================
# PERSONAGENS
# ==========================

jogador = {

    "nome": "Rebelião à Divindade",

    "vida_atual": 90,

    "vida_maxima": 90,

    "pocoes": 2,

    "critico": 20,

    "defesa": False,

    "ataques": (
        "Expurgo",
        "Rebelião"
    )
}

inimigo = {

    "nome": "Ascensão",

    "vida_atual": 95,

    "vida_maxima": 95,

    "pocoes": 1,

    "critico": 20,

    "defesa": False,

    "ataques": (
        "Quebra",
        "Irreal"
    )
}

ataques = {

    "Expurgo": {
        "dano": 5
    },

    "Rebelião": {
        "dano": 15
    },

    "Quebra": {
        "dano": 15
    },

    "Irreal": {
        "dano": 10
    }
}

pocoes = {

    "Poção Pequena": {
        "cura": 20
    },

    "Poção Média": {
        "cura": 40
    }
}

# ==========================
# PREPARAÇÃO DA BATALHA
# ==========================

vez_atual = random.choice(
    [
        "jogador",
        "inimigo"
    ]
)

fugiu = False

print("\n⚔ Preparando batalha...")

time.sleep(2)

mostrar_status(
    jogador,
    inimigo
)

time.sleep(2)

print("\n⚔ A batalha começou!")

time.sleep(1)

if vez_atual == "jogador":

    print("\n🎭 Você atacará primeiro!")

else:

    print("\n👁 Ascensão atacará primeiro!")

time.sleep(2)

# ==========================
# LOOP DA BATALHA
# ==========================

while (
    jogador["vida_atual"] > 0
    and inimigo["vida_atual"] > 0
):

    if vez_atual == "jogador":

        print("\n🎭 Seu turno!")

        time.sleep(1)

        resultado = turno_jogador(
            jogador,
            inimigo,
            ataques,
            pocoes
        )

        if resultado == "fugiu":

            fugiu = True

            break

        vez_atual = "inimigo"

    else:

        print("\n👁 Turno do inimigo!")

        time.sleep(1)

        turno_inimigo(
            inimigo,
            jogador,
            ataques
        )

        vez_atual = "jogador"

    time.sleep(2)

    print("\n📊 Status da batalha:")

    mostrar_status(
        jogador,
        inimigo
    )

    time.sleep(2)

# ==========================
# RESULTADO FINAL
# ==========================

print("\n==============================")

time.sleep(1)

if fugiu:

    print("🏃 Você fugiu da batalha!")

elif jogador["vida_atual"] <= 0:

    print("☠ Você foi derrotado!")
    time.sleep(1)
    print("A Ascensão destruiu toda a esperança.")

elif inimigo["vida_atual"] <= 0:

    print("🏆 Vitória!")
    time.sleep(1)
    print("A Rebelião à Divindade triunfou!")

print("==============================")