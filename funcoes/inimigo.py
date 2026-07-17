import random

from funcoes.combate import (
    causar_dano,
    aplicar_critico,
    aplicar_defesa,
    curar
)


def turno_inimigo(inimigo, jogador, ataques):

    # Chance de usar poção quando a vida estiver abaixo de 30%
    if (
        inimigo["vida_atual"] <= inimigo["vida_maxima"] * 0.3
        and inimigo["pocoes"] > 0
        and random.randint(1, 100) <= 10
    ):

        recuperado = curar(inimigo, 20)

        inimigo["pocoes"] -= 1

        print(
            f"\n🧪 {inimigo['nome']} usou uma poção!"
        )

        print(
            f"💚 Recuperou {recuperado} de vida!"
        )

        return

    ataque = random.choice(
        inimigo["ataques"]
    )

    dano = ataques[ataque]["dano"]

    dano = aplicar_critico(
        dano,
        inimigo["critico"]
    )

    dano = aplicar_defesa(
        jogador,
        dano
    )

    print(
        f"\n👁 {inimigo['nome']} usou {ataque}!"
    )

    causar_dano(
        jogador,
        dano
    )

    print(
        f"💥 Causou {dano} de dano!"
    )