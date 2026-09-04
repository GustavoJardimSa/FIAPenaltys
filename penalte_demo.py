def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('  |  '.join(linha))
        print('+----+----+----+----+----+----+----+----+----')


def fazer_jogada(tabuleiro, jogador):
    linha = int(input('Linha da jogada (0-4): '))
    coluna = int(input('Coluna da jogada (0-6): '))

    if tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = jogador
        return True
    else:
        print('Posição ocupada')
        return False


def jogo():
    tabuleiro = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]

    jogador = 'C'

    while True:
        mostrar_tabuleiro(tabuleiro)

        print(f'Vez do jogador {jogador}')

        jogada = fazer_jogada(tabuleiro, jogador)

        if not jogada:
            continue

        if jogador == 'C':
            jogador = 'G'
        else:
            jogador = 'C'


jogo()
