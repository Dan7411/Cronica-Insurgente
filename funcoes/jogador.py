import random
import time

from funcoes.combate import (
    causar_dano,
    aplicar_critico,
    curar,
    ativar_defesa
)


def turno_jogador(jogador, inimigo, ataques, pocoes):

    print("\nO que deseja fazer?")

    print("1 - Atacar")
    print("2 - Usar Poção")
    print("3 - Fugir")
    print("4 - Passar turno")
    print("5 - Defender")

    while True:

        try:

            escolha = int(input("\nEscolha: "))

            if escolha in [1, 2, 3, 4, 5]:
                break

            print("Escolha inválida!")

        except ValueError:

            print("Digite apenas números!")

    # ==========================
    # ATAQUE
    # ==========================

    if escolha == 1:

        print("\n========================")
        print("Escolha seu ataque:")

        for indice, ataque in enumerate(
            jogador["ataques"],
            start=1
        ):

            print(f"{indice} - {ataque}")

        while True:

            try:

                escolha_ataque = int(input("\nNúmero: "))

                if 1 <= escolha_ataque <= len(jogador["ataques"]):
                    break

                print("Ataque inválido!")

            except ValueError:

                print("Digite apenas números!")

        nome_ataque = jogador["ataques"][
            escolha_ataque - 1
        ]

        ataque = ataques[nome_ataque]

        dano = ataque["dano"]

        dano = aplicar_critico(
            dano,
            jogador["critico"]
        )

        print(
            f"\n⚔ {jogador['nome']} usou {nome_ataque}!"
        )

        causar_dano(
            inimigo,
            dano
        )

        print(
            f"💥 Causou {dano} de dano!"
        )

    # ==========================
    # POÇÃO
    # ==========================

    elif escolha == 2:

        if jogador["pocoes"] <= 0:

            print("\nVocê não possui poções!")

            time.sleep(1)

            return None

        print("\nPoções disponíveis:")

        nomes_pocoes = list(
            pocoes.keys()
        )

        for indice, nome in enumerate(
            nomes_pocoes,
            start=1
        ):

            print(f"{indice} - {nome}")

        while True:

            try:

                escolha_pocao = int(
                    input("\nEscolha a poção: ")
                )

                if 1 <= escolha_pocao <= len(nomes_pocoes):
                    break

                print("Poção inválida!")

            except ValueError:

                print("Digite apenas números!")

        nome_pocao = nomes_pocoes[
            escolha_pocao - 1
        ]

        cura_real = curar(
            jogador,
            pocoes[nome_pocao]["cura"]
        )

        jogador["pocoes"] -= 1

        print(
            f"\n🧪 {jogador['nome']} usou {nome_pocao}!"
        )

        print(
            f"💚 Recuperou {cura_real} HP!"
        )

    # ==========================
    # FUGIR
    # ==========================

    elif escolha == 3:

        chance = random.randint(1, 100)

        if chance <= 50:

            print("\n🏃 Você conseguiu fugir!")

            return "fugiu"

        else:

            print("\n❌ A fuga falhou!")

    # ==========================
    # PASSAR TURNO
    # ==========================

    elif escolha == 4:

        print("\n⏳ Você passou o turno!")

    # ==========================
    # DEFENDER
    # ==========================

    elif escolha == 5:

        ativar_defesa(
            jogador
        )

    time.sleep(1)

    return None