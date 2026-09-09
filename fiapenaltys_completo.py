# VERSÃO MAIS COMPLETA DO APLICATIVO - IGNORAR POR ENQUANTO, A DECIDIR SE SERÁ USADA

import random

def criar_gol():
    return [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',],
    ]

def criar_gol_visual():
    return [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]

def mostrar_gol(gol_visual):
    print('\n                                    FIAPENALTYS')
    print('             ESQUERDA                MEIO                    DIREITA')
    print('    ┌───────────────────────┬───────────────────────┬───────────────────────┐')

    for linha in range(3):
        print('    │                       │                       │                       │')

        texto_linha = '    │'

        for coluna in range(3):
            texto_linha += f'{gol_visual[linha][coluna]:^23}│'

        print(texto_linha)
        print('    │                       │                       │                       │')

        if linha < 2:
            print('    ├───────────────────────┼───────────────────────┼───────────────────────┤')

    print('    └───────────────────────┴───────────────────────┴───────────────────────┘')

def posicao_batedor():
    while True:
        try:
            escolha_chute = int(input('Escolha a região do chute (1-9): '))

            if escolha_chute > 0 and escolha_chute < 10:
                return escolha_chute
            else:
                print('Posição inválida. Tente novamente.')
        except ValueError:
            print('Entrada inválida. Digite números inteiros para a posição do chute.')

def posicao_goleiro():
    while True:
        try:
            escolha_defesa = int(input('Escolha onde o goleiro irá defender (1-9): '))

            if escolha_defesa > 0 and escolha_defesa < 10:
                return escolha_defesa
            else:
                print('Posição inválida. Tente novamente.')
        except ValueError:
            print('Entrada inválida. Digite números inteiros para posição da defesa.')

def sortear_posicao_exata(regiao):
    # LINHAS
    if regiao == 1 or regiao == 2 or regiao == 3:
        linha = random.randint(0, 1)

    elif regiao == 4 or regiao == 5 or regiao == 6:
        linha = random.randint(2, 3)

    else:
        linha = random.randint(4, 5)

    # COLUNAS
    if regiao == 1 or regiao == 4 or regiao == 7:
        coluna = random.randint(0, 3)

    elif regiao == 2 or regiao == 5 or regiao == 8:
        coluna = random.randint(4, 7)

    else:
        coluna = random.randint(8, 11)

    return linha, coluna

def marcar_regiao_visual(gol_visual, regiao, simbolo):
    linha_visual = (regiao - 1) // 3
    coluna_visual = (regiao - 1) % 3

    gol_visual[linha_visual][coluna_visual] = simbolo


gol_interno = criar_gol()
gol_visual = criar_gol_visual()

mostrar_gol(gol_visual)

# DECISÃO BATEDOR
regiao_batedor = posicao_batedor()
marcar_regiao_visual(gol_visual, regiao_batedor, 'X CHUTE X')
mostrar_gol(gol_visual)

linha, coluna = sortear_posicao_exata(regiao_batedor)
gol_interno[linha][coluna] = 'O'

# DECISÃO GOLEIRO
regiao_goleiro = posicao_goleiro()

marcar_regiao_visual(gol_visual, regiao_goleiro, 'X GOLEIRO X')
mostrar_gol(gol_visual)

linha, coluna = sortear_posicao_exata(regiao_goleiro)
gol_interno[linha][coluna] = 'O'
