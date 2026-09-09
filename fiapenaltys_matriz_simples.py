# CÓDIGO ANTIGO COM UMA MATRIZ SIMPLES
import os

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

def escolher_chute():
    while True:
        try:
            linha_chute = int(input('Linha do chute (1-5): '))
            coluna_chute = int(input('Coluna do chute (1-8): '))

            if linha_chute > 0 and linha_chute <= 5 and coluna_chute > 0 and coluna_chute <= 8:
                return linha_chute - 1, coluna_chute - 1

            print('Linha ou coluna inválida. Tente novamente.')

        except ValueError:
            print('Entrada inválida. Digite números inteiros.')

def escolher_defesa():
    while True:
        try:
            linha_defesa = int(input('Linha da defesa (1-5): '))
            coluna_defesa = int(input('Coluna da defesa (1-8): '))

            if linha_defesa > 0 and linha_defesa <= 5 and coluna_defesa > 0 and coluna_defesa <= 8:
                return linha_defesa - 1, coluna_defesa - 1

            print('Linha ou coluna invalida. Tente novamente')

        except ValueError:
            print('Entrada inválida. Digite números inteiros')

def confirmar_chute(gol):
    while True:
        linha_chute, coluna_chute = escolher_chute()

        gol[linha_chute][coluna_chute] = 'O'
        mostrar_gol(gol)

        confirmacao = input(
            'Pressione ENTER ou Y para confirmar. '
            'Digite N para escolher novamente: '
        ).strip().lower()

        if confirmacao == '' or confirmacao == 'y':
            gol[linha_chute][coluna_chute] = ' '
            os.system('cls')

            return linha_chute, coluna_chute

        elif confirmacao == 'n':
            gol[linha_chute][coluna_chute] = ' '
            os.system('cls')
            mostrar_gol(gol)

        else:
            print('Opção inválida. Escolha novamente.')
            gol[linha_chute][coluna_chute] = ' '

def confirmar_defesa(gol):
    while True:
        linha_defesa, coluna_defesa = escolher_defesa()

        gol[linha_defesa][coluna_defesa] = 'G'
        mostrar_gol(gol)

        confirmacao = input(
            'Pressione ENTER ou Y para confirmar a defesa. '
            'Digite N para escolher novamente: '
        ).strip().lower()

        if confirmacao == '' or confirmacao == 'y':
            gol[linha_defesa][coluna_defesa] = ' '
            os.system('cls')

            return linha_defesa, coluna_defesa

        elif confirmacao == 'n':
            gol[linha_defesa][coluna_defesa] = ' '
            os.system('cls')
            mostrar_gol(gol)

        else:
            print('Opção inválida. Escolha novamente.')
            gol[linha_defesa][coluna_defesa] = ' '

def main():
    gol = criar_gol()
    mostrar_gol(gol)

    # ESCOLHA DO BATEDOR
    linha_chute, coluna_chute = confirmar_chute(gol)

    # ESCOLHA DO GOLEIRO
    print('VEZ DO GOLEIRO')
    mostrar_gol(gol)

    linha_defesa, coluna_defesa = confirmar_defesa(gol)


main()