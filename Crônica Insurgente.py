import random
import time
from funcoes.combate import (
    aplicar_critico,
    causar_dano,
    curar,
    ativar_defesa,
    aplicar_defesa
)

# ==========================================
#              APRESENTAÇÃO
# ==========================================


print("=" * 40)
print("       CRÔNICA INSURGENTE")
print("=" * 40)


print("""
1 - Ver introdução e sinopse
2 - Pular introdução e ver apenas sinopse
3 - Pular tudo e iniciar batalha
""")


while True:

    escolha_inicio = input(
        "\nEscolha: "
    )

    if escolha_inicio in ["1", "2", "3"]:
        break

    else:
        print(
            "Digite apenas 1, 2 ou 3!"
        )


# ==========================================
#              INTRODUÇÃO
# ==========================================

if escolha_inicio == "1":

    print("\nBem-vindo, viajante.")

    time.sleep(1)

    print("""
Neste jogo, você controlará um mestre espiritual
em batalhas por turnos contra entidades poderosas.

Use ataques, estratégias e poções para sobreviver
até derrotar seu inimigo.
""")

    time.sleep(2)



# ==========================================
#                SINOPSE
# ==========================================

if escolha_inicio in ["1", "2"]:

    print("\nSinopse:")

    time.sleep(1)

    print("""
O mundo foi consumido pela miséria e pela discórdia.

Nem sempre foi assim.
Antigamente, a natureza florescia e a vida era abundante.

Por causa da ganância da humanidade,
o antigo guardião da natureza despertou.

Agora, apenas um transcendente é capaz
de impedir que toda a existência seja destruída.

Sua vontade será sua maior arma.
""")

    time.sleep(3)

input("\nPressione ENTER para iniciar a batalha...")

print("\nPreparando combate...")
time.sleep(2)
            
# ==========================================
#      DICIONÁRIO DOS PERSONAGENS
# ==========================================

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

# ==========================================
#         DICIONÁRIO DE ATAQUES
# ==========================================

ataques = {

    # Ataque de múltiplos golpes
    "Expurgo": {

        "tipo": "multi_dano",

        "golpes": 5,

        "dano": 5
    },

    # Ataque com dano persistente
    "Rebelião": {

        "tipo": "dano_persistente",

        "dano": 10,

        "persistente": 5,

        "duracao": 3
    },

    # Ataques do inimigo
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

print("\n" + "=" * 40)
print("          STATUS INICIAL")
print("=" * 40)

print(
    f"\n{jogador['nome']} "
    f"-> {jogador['vida_atual']} HP"
)

print(
    f"{inimigo['nome']} "
    f"-> {inimigo['vida_atual']} HP"
)

print("=" * 40)

time.sleep(2)


# ==========================================
#        DEFINIR PRIMEIRO TURNO
# ==========================================

primeiro_turno = random.choice([
    "jogador",
    "inimigo"
])


if primeiro_turno == "jogador":

    print(
        f"\n⚔ {jogador['nome']} "
        "começará atacando!"
    )

else:

    print(
        f"\n⚔ {inimigo['nome']} "
        "começará atacando!"
    )


time.sleep(2)


# ==========================================
#        EFEITO PERSISTENTE
# ==========================================

efeito_persistente = {

    "ativo": False,

    "dano": 0,

    "duracao": 0
}


# ==========================================
#        VARIÁVEIS DE CONTROLE
# ==========================================

turno = 0

fugiu = False

# controla de quem é a vez
vez_atual = primeiro_turno


print("\nA batalha começou!")

time.sleep(2)

# ==========================================
#             LAÇO PRINCIPAL
# ==========================================

# Continua enquanto os dois estiverem vivos
while (
    jogador["vida_atual"] > 0
    and inimigo["vida_atual"] > 0
):

    turno += 1

    print(
        f"\n========== TURNO {turno} =========="
    )

    time.sleep(1)


    # ==========================================
    #          VEZ DO JOGADOR
    # ==========================================

    if vez_atual == "jogador":

        print(
            f"\n🎭 Vez de "
            f"{jogador['nome']}!"
        )

        time.sleep(1)


        print("\nO que deseja fazer?")

        print("1 - Atacar")
        print("2 - Usar Poção")
        print("3 - Fugir")
        print("4 - Passar turno")
        print("5 - Defender")


        # Proteção contra letras ou símbolos
        while True:

            try:

                acao = int(
                    input("\nEscolha: ")
                )

                break

            except ValueError:

                print(
                    "\nDigite apenas números!"
                )


        # ==========================================
        #              ATACAR
        # ==========================================

        if acao == 1:

            print(
                "\nEscolha seu ataque:"
            )


            for indice, ataque in enumerate(
                jogador["ataques"],
                start=1
            ):

                print(
                    f"{indice} - {ataque}"
                )


            while True:

                try:

                    escolha_ataque = int(
                        input(
                            "\nDigite o número: "
                        )
                    )

                    break

                except ValueError:

                    print(
                        "\nDigite apenas números!"
                    )

        # ==========================================
        #        EXECUTAR ATAQUE ESCOLHIDO
        # ==========================================

        if (
            1 <= escolha_ataque
            <= len(jogador["ataques"])
        ):

            ataque_escolhido = (
                jogador["ataques"]
                [escolha_ataque - 1]
            )


            dados_ataque = ataques[
                ataque_escolhido
            ]


            print(
                f"\n⚔ {jogador['nome']} "
                f"usou {ataque_escolhido}!"
            )

            time.sleep(1)


            # ==========================================
            #              MULTI DANO
            # ==========================================

            if (
                dados_ataque["tipo"]
                == "multi_dano"
            ):

                golpes = random.randint(
                    1,
                    dados_ataque["golpes"]
                )


                dano_total = 0


                for golpe in range(golpes):

                    dano = (
                        dados_ataque["dano"]
                    )

                    dano_total += dano


                    print(
                        f"💥 Golpe "
                        f"{golpe + 1} "
                        f"causou "
                        f"{dano} de dano!"
                    )

                    time.sleep(0.7)



                inimigo["vida_atual"] -= (
                    dano_total
                )


                if inimigo["vida_atual"] < 0:

                    inimigo["vida_atual"] = 0



                print(
                    f"\nDano total causado: "
                    f"{dano_total}"
                )

                time.sleep(1)



            # ==========================================
            #          DANO PERSISTENTE
            # ==========================================

            elif (
                dados_ataque["tipo"]
                == "dano_persistente"
            ):


                dano = dados_ataque["dano"]

                dano = aplicar_critico(
    dano,
    jogador["critico"]
)


                inimigo["vida_atual"] -= dano



                if inimigo["vida_atual"] < 0:

                    inimigo["vida_atual"] = 0



                print(
                    f"🔥 Causou "
                    f"{dano} de dano inicial!"
                )


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



                print(
                    "\nO inimigo foi "
                    "afetado por um "
                    "dano persistente!"
                )


                time.sleep(1)



            # ==========================================
            #              DANO NORMAL
            # ==========================================

            else:


                dano = dados_ataque["dano"]


                inimigo["vida_atual"] -= dano



                if inimigo["vida_atual"] < 0:

                    inimigo["vida_atual"] = 0



                print(
                    f"Causou "
                    f"{dano} de dano!"
                )


                time.sleep(1)



        else:

            print(
                "\nAtaque inválido!"
            )

            time.sleep(1)

 # ==========================================
 #              Defender
 # ==========================================

    elif acao == 5:

     ativar_defesa(jogador)

     time.sleep(1)

        # ==========================================
        #              FUGIR DA BATALHA
        # ==========================================

    elif acao == 3:

            chance_fuga = random.randint(1, 100)

            if chance_fuga <= 50:

                print(
                    "\n🏃 Você conseguiu fugir!"
                )

                fugiu = True

                break

            else:

                print(
                    "\n❌ A fuga falhou!"
                )

                time.sleep(1)

    # ==========================================
    #             Passar Turno
    # ==========================================

    elif acao == 4:

            print(
                "\n⏳ Você passou o turno!"
            )

            time.sleep(1)

        # ==========================================
        #             USAR POÇÃO
        # ==========================================

    elif acao == 2:


            if jogador["pocoes"] > 0:


                print(
                    "\nPoções disponíveis:"
                )


                for nome_pocao, dados in pocoes.items():

                    print(
                        f"- {nome_pocao} "
                        f"(cura {dados['cura']} HP)"
                    )


                escolha_pocao = input(
                    "\nDigite o nome da poção: "
                )


                if escolha_pocao in pocoes:


                    cura = pocoes[
                        escolha_pocao
                    ]["cura"]


                    vida_antes = (
                        jogador["vida_atual"]
                    )


                    jogador["vida_atual"] += cura



                    # impede ultrapassar vida máxima
                    if (
                        jogador["vida_atual"]
                        > jogador["vida_maxima"]
                    ):

                        jogador["vida_atual"] = (
                            jogador["vida_maxima"]
                        )



                    jogador["pocoes"] -= 1



                    cura_real = (
                        jogador["vida_atual"]
                        - vida_antes
                    )


                    print(
                        f"\n🧪 {jogador['nome']} "
                        f"usou {escolha_pocao}!"
                    )


                    print(
                        f"Recuperou "
                        f"{cura_real} HP!"
                    )


                    print(
                        f"Poções restantes: "
                        f"{jogador['pocoes']}"
                    )


                    time.sleep(1)



                else:


                    print(
                        "\nPoção inválida!"
                    )


                    time.sleep(1)



            else:


                print(
                    "\nVocê não possui poções!"
                )


                time.sleep(1)



        # ==========================================
        #          OPÇÃO INVÁLIDA
        # ==========================================

    else:


      print(
                "\nOpção inválida!"
            )


    time.sleep(1)



    # ==========================================
    #          DANO PERSISTENTE
    # ==========================================

    if efeito_persistente["ativo"]:


        print(
            "\n🔥 O efeito persistente "
            "está causando dano!"
        )

        time.sleep(1)



        inimigo["vida_atual"] -= (
            efeito_persistente["dano"]
        )



        if inimigo["vida_atual"] < 0:

            inimigo["vida_atual"] = 0



        print(
            f"O inimigo perdeu "
            f"{efeito_persistente['dano']} HP!"
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


        time.sleep(1)



    # ==========================================
    #       VERIFICA DERROTA DO INIMIGO
    # ==========================================

    if inimigo["vida_atual"] <= 0:

        break



    # passa a vez para o inimigo

    vez_atual = "inimigo"

    # ==========================================
    #              TURNO DO INIMIGO
    # ==========================================

    if vez_atual == "inimigo":


        print(
            f"\n👁 Agora é a vez de "
            f"{inimigo['nome']}!"
        )


        time.sleep(1.5)



        # ==========================================
        #        IA DE CURA DO INIMIGO
        # ==========================================


        vida_limite = (
            inimigo["vida_maxima"]
            * 0.30
        )


        # Se a vida estiver abaixo de 30%
        # o inimigo pode tentar se curar

        if (
            inimigo["vida_atual"]
            <= vida_limite

            and inimigo["pocoes"] > 0
        ):


            chance_cura = random.randint(
                1,
                3
            )


            # 33% de chance de usar poção

            if chance_cura == 1:


                nome_pocao = random.choice(
                    list(pocoes.keys())
                )


                cura = pocoes[
                    nome_pocao
                ]["cura"]


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



                inimigo["pocoes"] -= 1



                cura_real = (
                    inimigo["vida_atual"]
                    - vida_antes
                )



                print(
                    f"\n🧪 {inimigo['nome']} "
                    f"usou {nome_pocao}!"
                )


                time.sleep(1)



                print(
                    f"Recuperou "
                    f"{cura_real} HP!"
                )


                print(
                    f"Poções restantes: "
                    f"{inimigo['pocoes']}"
                )


                time.sleep(2)



                # termina o turno do inimigo

                vez_atual = "jogador"

                continue

        # ==========================================
        #           ATAQUE DO INIMIGO
        # ==========================================


        ataque_inimigo = random.choice(
            inimigo["ataques"]
        )


        dados_ataque = ataques[
            ataque_inimigo
        ]


        print(
            f"\n⚔ {inimigo['nome']} "
            f"usou {ataque_inimigo}!"
        )


        time.sleep(1)



        # ==========================================
        #          ATAQUE NORMAL DO INIMIGO
        # ==========================================


        if (
            dados_ataque["tipo"]
            == "normal"
        ):


            dano = dados_ataque["dano"]


            dano = aplicar_defesa(
                jogador,
                dano
            )


            jogador["vida_atual"] -= dano


            jogador["vida_atual"] -= dano



            if jogador["vida_atual"] < 0:

                jogador["vida_atual"] = 0



            print(
                f"💥 {jogador['nome']} "
                f"perdeu {dano} HP!"
            )


            time.sleep(1)



        # ==========================================
        #          CASO TENHA OUTRO TIPO
        #          DE ATAQUE NO FUTURO
        # ==========================================

        else:


            dano = dados_ataque["dano"]


            jogador["vida_atual"] -= dano



            if jogador["vida_atual"] < 0:

                jogador["vida_atual"] = 0



            print(
                f"💥 Causou "
                f"{dano} de dano!"
            )


            time.sleep(1)



        # ==========================================
        #          PASSA A VEZ
        # ==========================================

        vez_atual = "jogador"


        time.sleep(1)

        # ==========================================
        #          STATUS ATUALIZADO
        # ==========================================


        def barra_vida(atual, maxima):

            tamanho = 20

            preenchido = int(
                (atual / maxima)
                * tamanho
            )

            vazio = tamanho - preenchido

            return (
                "█" * preenchido
                +
                "░" * vazio
            )



        print(
            "\n" + "=" * 40
        )

        print(
            "             STATUS"
        )

        print(
            "=" * 40
        )



        print(
            f"\n{jogador['nome']}"
        )

        print(
            f"[{barra_vida(
                jogador['vida_atual'],
                jogador['vida_maxima']
            )}]"
        )

        print(
            f"HP: "
            f"{jogador['vida_atual']}/"
            f"{jogador['vida_maxima']}"
        )



        print(
            f"\n{inimigo['nome']}"
        )

        print(
            f"[{barra_vida(
                inimigo['vida_atual'],
                inimigo['vida_maxima']
            )}]"
        )

        print(
            f"HP: "
            f"{inimigo['vida_atual']}/"
            f"{inimigo['vida_maxima']}"
        )



        print(
            "\n" + "=" * 40
        )


        time.sleep(2)



        # ==========================================
        #       VERIFICAÇÃO DE DERROTA
        # ==========================================


        if (
            jogador["vida_atual"]
            <= 0
        ):

            break


        if (
            inimigo["vida_atual"]
            <= 0
        ):

            break



        print(
            "\nA batalha continua..."
        )


        time.sleep(1)

# ==========================================
#              FIM DE JOGO
# ==========================================


print(
    "\n" + "=" * 40
)

print(
    "          FIM DA BATALHA"
)

print(
    "=" * 40
)


time.sleep(2)



# ==========================================
#          RESULTADO FINAL
# ==========================================

if fugiu:

    print(
        "\n🌑 A batalha foi encerrada."
    )

    print(
        f"{jogador['nome']} escapou!"
    )

    time.sleep(2)

    exit()

if jogador["vida_atual"] <= 0:


    print(
        f"\n☠ {jogador['nome']} "
        "foi derrotado!"
    )


    time.sleep(1)


    print(
        f"🏆 {inimigo['nome']} "
        "venceu a batalha!"
    )



elif inimigo["vida_atual"] <= 0:


    print(
        f"\n☠ {inimigo['nome']} "
        "foi derrotado!"
    )


    time.sleep(1)


    print(
        f"🏆 {jogador['nome']} "
        "venceu a batalha!"
    )



time.sleep(2)



print(
    "\nObrigado por jogar "
    "CRÔNICA INSURGENTE!"
)


print(
    "=" * 40
)

# ==========================================
#             FUNÇÕES AUXILIARES
# ==========================================


# ==========================================
#           BARRA DE VIDA
# ==========================================

def barra_vida(atual, maxima):

    tamanho = 20

    porcentagem = atual / maxima

    preenchido = int(
        porcentagem * tamanho
    )

    vazio = tamanho - preenchido


    return (
        "█" * preenchido
        +
        "░" * vazio
    )



# ==========================================
#        MOSTRAR STATUS
# ==========================================

def mostrar_status():

    print(
        "\n" + "=" * 40
    )

    print(
        "             STATUS"
    )

    print(
        "=" * 40
    )


    print(
        f"\n{jogador['nome']}"
    )

    print(
        f"[{barra_vida(
            jogador['vida_atual'],
            jogador['vida_maxima']
        )}]"
    )

    print(
        f"HP: "
        f"{jogador['vida_atual']}/"
        f"{jogador['vida_maxima']}"
    )


    print(
        f"\n{inimigo['nome']}"
    )

    print(
        f"[{barra_vida(
            inimigo['vida_atual'],
            inimigo['vida_maxima']
        )}]"
    )

    print(
        f"HP: "
        f"{inimigo['vida_atual']}/"
        f"{inimigo['vida_maxima']}"
    )


    print(
        "\n" + "=" * 40
    )


    time.sleep(1)



# ==========================================
#        APLICAR DANO COM SEGURANÇA
# ==========================================

def causar_dano(alvo, dano):

    alvo["vida_atual"] -= dano


    if alvo["vida_atual"] < 0:

        alvo["vida_atual"] = 0



# ==========================================
#              CURAR PERSONAGEM
# ==========================================

def curar(personagem, quantidade):

    vida_antiga = (
        personagem["vida_atual"]
    )


    personagem["vida_atual"] += quantidade


    if (
        personagem["vida_atual"]
        > personagem["vida_maxima"]
    ):

        personagem["vida_atual"] = (
            personagem["vida_maxima"]
        )


    cura_real = (
        personagem["vida_atual"]
        -
        vida_antiga
    )


    return cura_real

# ==========================================
#        ENTRADA DE NÚMEROS SEGURA
# ==========================================

def escolher_numero(mensagem):

    while True:

        try:

            numero = int(
                input(mensagem)
            )

            return numero


        except ValueError:

            print(
                "\nDigite apenas números!"
            )




