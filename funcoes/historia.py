import time


def mostrar_menu_inicio():

    print("""
====================================
        CRÔNICA INSURGENTE
====================================
""")

    print("Uma jornada está prestes a começar...")

    time.sleep(2)

    print("""
1 - Ver introdução e sinopse
2 - Pular introdução e ver apenas sinopse
3 - Pular tudo e iniciar batalha
""")

    while True:

        escolha = input("\nEscolha: ")

        if escolha in ["1", "2", "3"]:

            return escolha

        print("\nDigite apenas 1, 2 ou 3!")


def mostrar_introducao():

    print("\nAs montanhas estremecem.")

    time.sleep(2)

    print("\nO céu perdeu sua luz.")

    time.sleep(2)

    print("""
Uma presença ancestral desperta.

Seu poder faz o próprio mundo
tremer diante da inevitável destruição.
""")

    time.sleep(3)

    print("""
Entre milhões de vidas,
apenas um cultivador ousou desafiar
aquele que se proclamou uma divindade.
""")

    time.sleep(3)


def mostrar_sinopse():

    print("\n📜 Sinopse")

    time.sleep(1)

    print("""
Durante séculos, a humanidade explorou
a natureza sem limites.

Florestas desapareceram.

Rios secaram.

Montanhas foram reduzidas a cinzas.
""")

    time.sleep(3)

    print("""
Quando o equilíbrio finalmente foi rompido,
o Guardião da Natureza despertou.

Agora conhecido como Ascensão,
ele decidiu apagar toda a civilização.
""")

    time.sleep(3)

    print("""
Você é o último transcendente.

Seu caminho será marcado por batalhas,
sacrifícios e escolhas.

O destino do mundo depende apenas
da sua força.
""")

    time.sleep(4)