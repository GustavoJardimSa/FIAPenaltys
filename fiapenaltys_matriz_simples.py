import os
import random

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

def limpar_gol(gol):
    for linha in range(5):
        for coluna in range(8):
            gol[linha][coluna] = ' '

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

def verificar_fim_antecipado(gols_time_1, gols_time_2, cobrancas_time_1, cobrancas_time_2):
    restantes_time_1 = 5 - (cobrancas_time_1)
    restantes_time_2 = 5 - (cobrancas_time_2)

    if gols_time_1 > gols_time_2 + restantes_time_2:
        return True
    if gols_time_2 > gols_time_1 + restantes_time_1:
        return True

    return False

def main():
    gol = criar_gol()

    print('==========================')
    print('       FIAPENALTYS')
    print('==========================')

    time_1 = input('Digite o nome do Time 1: ')
    time_2 = input('Digite o nome do Time 2: ')

    gols_time_1 = 0
    gols_time_2 = 0

    historico_time_1 = ['-', '-', '-', '-', '-']
    historico_time_2 = ['-', '-', '-', '-', '-']

    #JOGO PRINCIPAL
    for rodada in range(1,6):
        os.system('cls')

        print(f'\n========== RODADA {rodada} DE 5 ==========')
        mostrar_placar(
            time_1, ''.join(historico_time_1),
            time_2, ''.join(historico_time_2)
        )

        #COBRANÇA DO TIME 1
        resultado = executar_cobranca(gol, time_1, time_2)

        if resultado == 'GOL':
            gols_time_1 += 1
            historico_time_1[rodada - 1] = 'O'
        else:
            historico_time_1[rodada - 1] = 'X'

        os.system('cls')

        print(f'\n========== RODADA {rodada} DE 5 ==========')
        mostrar_placar(
            time_1, ''.join(historico_time_1),
            time_2, ''.join(historico_time_2)
        )

        if verificar_fim_antecipado(gols_time_1, gols_time_2, rodada, rodada -1):
            break
    
        #COBRANÇA DO TIME 2
        resultado = executar_cobranca(gol, time_2, time_1)

        if resultado == 'GOL':
            gols_time_2 += 1
            historico_time_2[rodada - 1] = 'O'
        else:
            historico_time_2[rodada - 1] = 'X'

        os.system('cls')

        print(f'\n========== RODADA {rodada} DE 5 ==========')
        mostrar_placar(
            time_1, ''.join(historico_time_1),
            time_2, ''.join(historico_time_2)
        )

        if verificar_fim_antecipado(gols_time_1, gols_time_2, rodada, rodada):
            break

        if rodada < 5:
            input('Pressione ENTER para iniciar a próxima rodada.')

# COBRANÇAS ALTERNADAS
    if gols_time_1 == gols_time_2:
       print('DEU EMPATE! QUE JOGO EMOCIONANTE!')
       print('AGORA VAMOS PARA AS COBRANÇAS ALTERNADAS') 
       input('Pressione ENTER para continuar.')

       rodada_alternada = 1

       while gols_time_1 == gols_time_2:
            print(f'\n===== RODADA ALTERNADA {rodada_alternada} =====')
            mostrar_placar(
                time_1, ''.join(historico_time_1),
                time_2, ''.join(historico_time_2)
            )

            #COBRANÇA DO TIME 1
            resultado = executar_cobranca(gol, time_1, time_2)

            if resultado == 'GOL':
                gols_time_1 += 1
                historico_time_1.append('O')
            else:
                historico_time_1.append('X')

            os.system('cls')

            print(f'\n===== RODADA ALTERNADA {rodada_alternada} =====')
            mostrar_placar(
                time_1, ''.join(historico_time_1),
                time_2, ''.join(historico_time_2)
            )

            #COBRANÇA DO TIME 2
            resultado = executar_cobranca(gol, time_2, time_1)
            
            if resultado == 'GOL':
                gols_time_2 += 1
                historico_time_2.append('O')
            else:
                historico_time_2.append('X')

            os.system('cls')

            print(f'\n===== RODADA ALTERNADA {rodada_alternada} =====')
            mostrar_placar(
                time_1, ''.join(historico_time_1),
                time_2, ''.join(historico_time_2)
            )

            if gols_time_1 == gols_time_2:
                rodada_alternada += 1
                input('Pressione ENTER para a próxima rodada alternada.')

    #RESULTADO FINAL
    os.system('cls')

    print('\n==============================')
    print('        FIM DE JOGO')
    print('==============================')

    mostrar_placar(
        time_1, ''.join(historico_time_1),
        time_2, ''.join(historico_time_2)
    )

    print(f'Placar em gols: {gols_time_1} x {gols_time_2}')

    if gols_time_1 > gols_time_2:
        print(f'{time_1} SAI VENCEDOR!')
    else:
        print(f'{time_2} SAI VENCEDOR!')

main()