import random
import time

# ==========================================
#              APRESENTAÇÃO
# ==========================================

print("======== CRÔNICA INSURGENTE ========")

time.sleep(1)

print("\nBem-vindo, viajante.")

print("""
Neste jogo, você controlará um mestre espiritual
em batalhas por turnos contra entidades poderosas.

Use ataques e poções para sobreviver
até derrotar seu inimigo.
""")

# ==========================================
#        DICIONÁRIOS DOS PERSONAGENS
# ==========================================

jogador = {

    "nome": "Rebelião à Divindade",

    "vida_atual": 90,
    "vida_maxima": 90,

    "pocoes": 2,

    "ataques": (
        "Expurgo",
        "Rebelião"
    )
}

inimigo = {

    "nome": "Ascenção",

    "vida_atual": 95,
    "vida_maxima": 95,

    "pocoes": 1,

    "ataques": (
        "Quebra",
        "Irreal"
    )
}

# ==========================================
#         DICIONÁRIO DE ATAQUES
# ==========================================

ataques = {

    # ataque de vários golpes
    "Expurgo": {

        "tipo": "multi_dano",

        "golpes": 3,

        "dano": 5
    },

    # ataque com dano persistente
    "Rebelião": {

        "tipo": "dano_persistente",

        "dano": 10,

        "persistente": 5,

        "duracao": 3
    },

    # ataques do inimigo
    "Quebra": {

        "tipo": "normal",

        "dano": 25
    },

    "Irreal": {

        "tipo": "normal",

        "dano": 15
    }
}

# ==========================================
#         DICIONÁRIO DE POÇÕES
# ==========================================

pocoes = {

    "Poção Pequena": {

        "cura": 20
    },

    "Poção Média": {

        "cura": 40
    }
}

# ==========================================
#        STATUS INICIAL DA BATALHA
# ==========================================

print("\n========== STATUS ==========")

print(
    f"\n{jogador['nome']} -> "
    f"{jogador['vida_atual']} HP"
)

print(
    f"{inimigo['nome']} -> "
    f"{inimigo['vida_atual']} HP"
)

print("\n============================")

# ==========================================
#        QUEM COMEÇA PRIMEIRO
# ==========================================

primeiro_turno = random.choice([
    jogador["nome"],
    inimigo["nome"]
])

print(f"\n⚔ {primeiro_turno} atacará primeiro!")

# variável do efeito persistente
efeito_persistente = {

    "ativo": False,

    "dano": 0,

    "duracao": 0
}

turno = 0

# ==========================================
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
            dados_ataque = (
                ataques[ataque_escolhido]
            )

            print(
                f"\n{jogador['nome']} usou "
                f"{ataque_escolhido}!"
            )

            # ==========================================
            #            MULTI DANO
            # ==========================================

            if (
                dados_ataque["tipo"]
                == "multi_dano"
            ):

                dano_total = 0

                # repete os golpes
                for golpe in range(
                    dados_ataque["golpes"]
                ):

                    dano_total += (
                        dados_ataque["dano"]
                    )

                    print(
                        f"Golpe {golpe + 1} "
                        f"causou "
                        f"{dados_ataque['dano']} "
                        f"de dano!"
                    )

                inimigo["vida_atual"] -= (
                    dano_total
                )

                print(
                    f"\nDano total: "
                    f"{dano_total}"
                )

            # ==========================================
            #         DANO PERSISTENTE
            # ==========================================

            elif (
                dados_ataque["tipo"]
                == "dano_persistente"
            ):

                dano = dados_ataque["dano"]

                inimigo["vida_atual"] -= dano

                print(
                    f"Causou {dano} de dano!"
                )

                # ativa efeito persistente
                efeito_persistente = {

                    "ativo": True,

                    "dano": (
                        dados_ataque[
                            "persistente"
                        ]
                    ),

                    "duracao": (
                        dados_ataque[
                            "duracao"
                        ]
                    )
                }

            # ==========================================
            #              DANO NORMAL
            # ==========================================

            else:

                dano = dados_ataque["dano"]

                inimigo["vida_atual"] -= dano

                print(
                    f"Causou {dano} de dano!"
                )

        else:

            print("\nAtaque inválido!")

    # ==========================================
    #             USAR POÇÃO
    # ==========================================

    elif acao == 2:

        # verifica se possui poções
        if jogador["pocoes"] > 0:

            print("\nPoções disponíveis:")

            for nome_pocao, dados in (
                pocoes.items()
            ):

                print(
                    f"- {nome_pocao} "
                    f"(cura {dados['cura']})"
                )

            escolha_pocao = input(
                "\nDigite o nome da poção: "
            )

            # verifica se a poção existe
            if escolha_pocao in pocoes:

                cura = (
                    pocoes[
                        escolha_pocao
                    ]["cura"]
                )

                vida_antes = (
                    jogador["vida_atual"]
                )

                # usa a poção
                jogador["vida_atual"] += cura

                # impede ultrapassar vida máxima
                if (
                    jogador["vida_atual"]
                    > jogador["vida_maxima"]
                ):

                    jogador["vida_atual"] = (
                        jogador["vida_maxima"]
                    )

                # remove uma poção
                jogador["pocoes"] -= 1

                # calcula quanto curou
                cura_real = (
                    jogador["vida_atual"]
                    - vida_antes
                )

                print(
                    f"\n{jogador['nome']} usou "
                    f"{escolha_pocao}!"
                )

                print(
                    f"Recuperou "
                    f"{cura_real} de vida!"
                )

                print(
                    f"Poções restantes: "
                    f"{jogador['pocoes']}"
                )

            else:

                print("\nPoção inválida!")

        else:

            print(
                "\nVocê não possui poções!"
            )

    else:

        print("\nOpção inválida!")

    # ==========================================
    #        EFEITO PERSISTENTE
    # ==========================================

    if efeito_persistente["ativo"]:

        inimigo["vida_atual"] -= (
            efeito_persistente["dano"]
        )

        print(
            f"\n🔥 O efeito persistente "
            f"causou "
            f"{efeito_persistente['dano']} "
            f"de dano!"
        )

        efeito_persistente["duracao"] -= 1

        # encerra efeito
        if (
            efeito_persistente["duracao"]
            <= 0
        ):

            efeito_persistente["ativo"] = False

            print(
                "\nO efeito persistente terminou."
            )

    # verifica derrota do inimigo
    if inimigo["vida_atual"] <= 0:
        break

    # ==========================================
    #           TURNO DO INIMIGO
    # ==========================================

    print(
        f"\nAgora é a vez de "
        f"{inimigo['nome']}!"
    )

    # ==========================================
    #      IA DE CURA DO INIMIGO
    # ==========================================

    vida_limite = (
        inimigo["vida_maxima"] * 0.30
    )

    # verifica se vida está abaixo de 30%
    if (
        inimigo["vida_atual"]
        <= vida_limite
        and inimigo["pocoes"] > 0
    ):

        # 10% de chance de usar poção
        teste = random.randint(1, 10)

        if teste == 1:

            nome_pocao = random.choice(
                list(pocoes.keys())
            )

            cura = (
                pocoes[nome_pocao]["cura"]
            )

            vida_antes = (
                inimigo["vida_atual"]
            )

            inimigo["vida_atual"] += cura

            # impede ultrapassar vida máxima
            if (
                inimigo["vida_atual"]
                > inimigo["vida_maxima"]
            ):

                inimigo["vida_atual"] = (
                    inimigo["vida_maxima"]
                )

            # remove uma poção
            inimigo["pocoes"] -= 1

            cura_real = (
                inimigo["vida_atual"]
                - vida_antes
            )

            print(
                f"\n🧪 {inimigo['nome']} usou "
                f"{nome_pocao}!"
            )

            print(
                f"Recuperou "
                f"{cura_real} de vida!"
            )

            # termina turno do inimigo
            continue

    # ==========================================
    #         ATAQUE DO INIMIGO
    # ==========================================

    ataque_inimigo = random.choice(
        inimigo["ataques"]
    )

    dados_ataque = ataques[
        ataque_inimigo
    ]

    dano = dados_ataque["dano"]

    jogador["vida_atual"] -= dano

    print(
        f"\n⚔ {inimigo['nome']} usou "
        f"{ataque_inimigo}!"
    )

    print(
        f"{jogador['nome']} perdeu "
        f"{dano} de vida!"
    )

    # ==========================================
    #        STATUS ATUALIZADO
    # ==========================================

    print("\n========== STATUS ==========")

    print(
        f"\n{jogador['nome']} -> "
        f"{jogador['vida_atual']} HP"
    )

    print(
        f"{inimigo['nome']} -> "
        f"{inimigo['vida_atual']} HP"
    )

    print("\n============================")

# ==========================================
#              FIM DE JOGO
# ==========================================

print("\n========== FIM DA BATALHA ==========")

# jogador derrotado
if jogador["vida_atual"] <= 0:

    print(
        f"\n☠ {jogador['nome']} foi derrotado!"
    )

    print(
        f"🏆 {inimigo['nome']} venceu!"
    )

# inimigo derrotado
elif inimigo["vida_atual"] <= 0:

    print(
        f"\n☠ {inimigo['nome']} foi derrotado!"
    )

    print(
        f"🏆 {jogador['nome']} venceu!"
    )

print("\n====================================")