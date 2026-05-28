import random
import time

time.sleep(2)

# ==========================================
#              APRESENTAÇÃO
# ==========================================

print("======== CRÔNICA INSURGENTE ========")

time.sleep(2)

print("\nBem-vindo, viajante.")

time.sleep(2)

print("""
Neste jogo, você controlará um mestre espiritual
em batalhas por turnos contra entidades poderosas.

Use ataques estratégicos para derrotar seus inimigos
antes que sua vida chegue a zero.
""")

time.sleep(2)

print("Prepare-se para a batalha...\n")

# ==========================================
#        DICIONÁRIOS DE ENTIDADES
# ==========================================

jogador = {

    "nome": "Rebelião à Divindade",

    "vida_atual": 90,
    "vida_maxima": 90,

    "pocoes": 3,

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

    # MULTI DANO
    "Expurgo": {

        "tipo": "multi_dano",

        "golpes": 3,

        "dano": 5,

        "descricao": "Uma sequência de ataques espirituais."
    },

    # DANO PERSISTENTE
    "Rebelião": {

        "tipo": "dano_persistente",

        "dano": 10,

        "persistente": 5,

        "duracao": 3,

        "descricao": "Marca o inimigo com energia destrutiva."
    },

    "Quebra": {

        "tipo": "normal",

        "dano": 25,

        "descricao": "Um ataque brutal."
    },

    "Irreal": {

        "tipo": "normal",

        "dano": 15,

        "descricao": "Ataques ilusórios."
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
    },

    "Poção Suprema": {

        "cura": 999
    }
}

# ==========================================
#          STATUS INICIAL
# ==========================================

print("\n========== STATUS DA BATALHA ==========")

print(f"\nPersonagem: {jogador['nome']}")
print(
    f"Vida: "
    f"{jogador['vida_atual']}/"
    f"{jogador['vida_maxima']}"
)

print("\n------------------------------")

print(f"\nInimigo: {inimigo['nome']}")
print(
    f"Vida: "
    f"{inimigo['vida_atual']}/"
    f"{inimigo['vida_maxima']}"
)

print("\n=======================================\n")

# ==========================================
#         INÍCIO DO COMBATE
# ==========================================

primeiro_turno = random.choice([
    jogador["nome"],
    inimigo["nome"]
])

print("A batalha começou!\n")

print(f"⚔ {primeiro_turno} irá atacar primeiro!\n")

turno = 0

# ==========================================
#             LAÇO PRINCIPAL
# ==========================================

while (
    jogador["vida_atual"] > 0
    and inimigo["vida_atual"] > 0
):

    turno += 1

    print(f"\n========== TURNO {turno} ==========")

    print(
        f"\n{jogador['nome']}: "
        f"{jogador['vida_atual']} HP"
    )

    print(
        f"{inimigo['nome']}: "
        f"{inimigo['vida_atual']} HP"
    )

    # ==========================================
    #           TURNO DO JOGADOR
    # ==========================================

    print("\nO que deseja fazer?")
    print("1 - Atacar")
    print("2 - Usar Poção")

    acao = int(input("Escolha uma opção: "))

    # ==========================================
    #                ATACAR
    # ==========================================

    if acao == 1:

        print("\nEscolha um ataque:")

        for indice, ataque_nome in enumerate(
            jogador["ataques"],
            start=1
        ):

            print(f"{indice} - {ataque_nome}")

        escolha_ataque = int(
            input("\nDigite o número do ataque: ")
        )

        if (
            1 <= escolha_ataque
            <= len(jogador["ataques"])
        ):

            ataque_escolhido = (
                jogador["ataques"][
                    escolha_ataque - 1
                ]
            )

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

                for golpe in range(
                    dados_ataque["golpes"]
                ):

                    dano_total += (
                        dados_ataque["dano"]
                    )

                    print(
                        f"Golpe {golpe + 1} causou "
                        f"{dados_ataque['dano']} "
                        f"de dano!"
                    )

                dano = dano_total

            # ==========================================
            #         DANO PERSISTENTE
            # ==========================================

            elif (
                dados_ataque["tipo"]
                == "dano_persistente"
            ):

                dano = dados_ataque["dano"]

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
            #             DANO NORMAL
            # ==========================================

            else:

                dano = dados_ataque["dano"]

            inimigo["vida_atual"] -= dano

            print(
                f"\nCausou {dano} de dano!"
            )

        else:

            print("\nAtaque inválido!")

    # ==========================================
    #             USAR POÇÃO
    # ==========================================

    elif acao == 2:

        if jogador["pocoes"] > 0:

            print("\nPoções disponíveis:")

            for nome_pocao, dados in (
                pocoes.items()
            ):

                print(
                    f"- {nome_pocao} | "
                    f"Cura: {dados['cura']}"
                )

            escolha_pocao = input(
                "\nDigite o nome da poção: "
            )

            if escolha_pocao in pocoes:

                jogador["pocoes"] -= 1

                cura = (
                    pocoes[
                        escolha_pocao
                    ]["cura"]
                )

                vida_antes = (
                    jogador["vida_atual"]
                )

                jogador["vida_atual"] += cura

                if (
                    jogador["vida_atual"]
                    > jogador["vida_maxima"]
                ):

                    jogador["vida_atual"] = (
                        jogador["vida_maxima"]
                    )

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

                continue

            else:

                print("\nPoção inválida!")

        else:

            print(
                "\nVocê não possui "
                "poções disponíveis!"
            )

    else:

        print("\nOpção inválida!")
        continue

    # ==========================================
    #        DANO PERSISTENTE
    # ==========================================

    if (
        "efeito_persistente" in locals()
        and efeito_persistente["ativo"]
    ):

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

        if (
            efeito_persistente["duracao"]
            <= 0
        ):

            efeito_persistente["ativo"] = False

            print(
                "\nO efeito persistente terminou."
            )

    # ==========================================
    #          VERIFICA VITÓRIA
    # ==========================================

    if inimigo["vida_atual"] <= 0:

        break

    # ==========================================
    #          TURNO DO INIMIGO
    # ==========================================

    print(
        f"\nAgora é a vez de "
        f"{inimigo['nome']}!"
    )

    # ==========================================
    #      INTELIGÊNCIA DO INIMIGO
    # ==========================================

    vida_limite = (
        inimigo["vida_maxima"] * 0.30
    )

    if (
        inimigo["vida_atual"]
        <= vida_limite
        and inimigo["pocoes"] > 0
    ):

        teste_cura = random.randint(1, 10)

        if teste_cura == 1:

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

            if (
                inimigo["vida_atual"]
                > inimigo["vida_maxima"]
            ):

                inimigo["vida_atual"] = (
                    inimigo["vida_maxima"]
                )

            cura_real = (
                inimigo["vida_atual"]
                - vida_antes
            )

            inimigo["pocoes"] -= 1

            print(
                f"\n🧪 {inimigo['nome']} usou "
                f"{nome_pocao}!"
            )

            print(
                f"{inimigo['nome']} recuperou "
                f"{cura_real} de vida!"
            )

            continue

    # ==========================================
    #          ATAQUE DO INIMIGO
    # ==========================================

    ataque_inimigo = random.choice(
        inimigo["ataques"]
    )

    dados_ataque = ataques[
        ataque_inimigo
    ]

    if (
        dados_ataque["tipo"]
        == "multi_dano"
    ):

        dano_total = 0

        for golpe in range(
            dados_ataque["golpes"]
        ):

            dano_total += (
                dados_ataque["dano"]
            )

        dano = dano_total

    elif (
        dados_ataque["tipo"]
        == "dano_persistente"
    ):

        dano = dados_ataque["dano"]

    else:

        dano = dados_ataque["dano"]

    jogador["vida_atual"] -= dano

    print(
        f"\n⚔ {inimigo['nome']} usou "
        f"{ataque_inimigo}!"
    )

    print(
        f"{jogador['nome']} recebeu "
        f"{dano} de dano!"
    )

    print(
        f"Vida atual de "
        f"{jogador['nome']}: "
        f"{jogador['vida_atual']}/"
        f"{jogador['vida_maxima']}"
    )

# ==========================================
#           RESULTADO FINAL
# ==========================================

if jogador["vida_atual"] <= 0:

    print(
        f"\n☠ {jogador['nome']} "
        f"foi derrotado!"
    )

    print(
        f"🏆 {inimigo['nome']} "
        f"venceu a batalha!"
    )

else:

    print(
        f"\n☠ {inimigo['nome']} "
        f"foi derrotado!"
    )

    print(
        f"🏆 {jogador['nome']} "
        f"venceu a batalha!"
    )