import os
import random

from gol import mostrar_gol, limpar_gol, calcular_chances

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

def definir_resultado(chance_defesa):
    numero_sorteado = random.randint(1,100)

    if numero_sorteado <= chance_defesa:
        return 'DEFESA'

    return 'GOL'

def mostrar_placar(time_1, gols_time_1, time_2, gols_time_2):
    print('\n==============================')
    print('       PLACAR')
    print(f'{time_1}: {gols_time_1}')
    print(f'{time_2}: {gols_time_2}')
    print('==============================\n')

def executar_cobranca(gol, time_batedor, time_goleiro):
    limpar_gol(gol)

    print(f'\n{time_batedor} está cobrando!')
    print(f'\n{time_goleiro} está defendendo!')

    mostrar_gol(gol)
    linha_chute, coluna_chute = confirmar_chute(gol)

    print(f'\nVEZ DO GOLEIRO DO {time_goleiro}')
    mostrar_gol(gol)

    linha_defesa, coluna_defesa = confirmar_defesa(gol)

    calcular_chances(gol, linha_defesa, coluna_defesa)
    chance_defesa = gol[linha_chute][coluna_chute]

    resultado = definir_resultado(chance_defesa)

    print(f'Resultado da cobrança: {resultado}')
    input('Pressione ENTER para continuar.')

    return resultado

def verificar_fim_antecipado(gols_time_1, gols_time_2, cobrancas_time_1, cobrancas_time_2):
    restantes_time_1 = 5 - (cobrancas_time_1)
    restantes_time_2 = 5 - (cobrancas_time_2)

    if gols_time_1 > gols_time_2 + restantes_time_2:
        return True
    if gols_time_2 > gols_time_1 + restantes_time_1:
        return True

    return False