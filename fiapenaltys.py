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
    print('       1     2     3     4     5     6     7     8')
    print('    ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐')

    for linha in range(5):
        texto_linha = f'{linha + 1}   │'

        for coluna in range(8):
            texto_linha += f'  {gol[linha][coluna]}  │'

        print(texto_linha)

        if linha < 4:
            print('    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤')

    print('    └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘')
    
gol = criar_gol()
mostrar_gol(gol)