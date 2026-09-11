def criar_gol():
    return [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]


def mostrar_gol(gol):
    print('\n                       FIAPENALTYS')
    print('        1     2     3     4     5     6     7     8')
    print('    ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐')

    for linha in range(5):
        texto_linha = f'{linha + 1}   │'

        for coluna in range(8):
            texto_linha += f'  {gol[linha][coluna]}  │'

        print(texto_linha)

        if linha < 4:
            print('    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤')
    print('    └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘')

def limpar_gol(gol):
    for linha in range(5):
        for coluna in range(8):
            gol[linha][coluna] = ' '

def calcular_chances(gol, linha_defesa, coluna_defesa):
    for linha in range(5):
        for coluna in range(8):
            distancia_linha = abs(linha - linha_defesa)
            distancia_coluna = abs(coluna - coluna_defesa)

            if distancia_linha == 0 and distancia_coluna == 0:
                gol[linha][coluna] = 100

            elif distancia_linha <= 1 and distancia_coluna <= 2:
                gol[linha][coluna] = 80

            elif distancia_linha <= 2 and distancia_coluna <= 3:
                gol[linha][coluna] = 40

            else:
                gol[linha][coluna] = 0