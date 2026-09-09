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



def mostrar_gol(gol):
    print('\n                       FIAPENALTYS')
    print('       1     2     3     4     5     6     7     8     9    10    11    12')
    print('    ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐')

    for linha in range(6):
        texto_linha = f'{linha + 1}   │'

        for coluna in range(12):
            texto_linha += f'  {gol[linha][coluna]}  │'

        print(texto_linha)

        if linha < 5:
            print('    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤')

    print('    └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘')

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

gol = criar_gol()
mostrar_gol(gol)

regiao_batedor = posicao_batedor()
linha, coluna = sortear_posicao_exata(regiao_batedor)

gol[linha][coluna] = 'O'
mostrar_gol(gol)