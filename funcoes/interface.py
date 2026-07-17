def barra_vida(atual, maxima):

    tamanho = 24

    cheio = int(
        atual / maxima * tamanho
    )

    vazio = tamanho - cheio

    return (
        "▉" * cheio +
        "░" * vazio
    )


def mostrar_status(jogador, inimigo):

    print("\n" + "=" * 50)
    print("             ⚔ STATUS DA BATALHA ⚔")
    print("=" * 50)

    print(f"\n🎭 {jogador['nome']}")
    print(
        f"❤ [{barra_vida(jogador['vida_atual'], jogador['vida_maxima'])}]"
    )
    print(
        f"HP: {jogador['vida_atual']}/{jogador['vida_maxima']}"
    )
    print(
        f"🧪 Poções: {jogador['pocoes']}"
    )

    print("\n" + "-" * 50)

    print(f"\n👁 {inimigo['nome']}")
    print(
        f"❤ [{barra_vida(inimigo['vida_atual'], inimigo['vida_maxima'])}]"
    )
    print(
        f"HP: {inimigo['vida_atual']}/{inimigo['vida_maxima']}"
    )
    print(
        f"🧪 Poções: {inimigo['pocoes']}"
    )

    print("\n" + "=" * 50)