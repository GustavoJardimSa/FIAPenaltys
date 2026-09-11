import os

from gol import criar_gol
from sistema_jogo import(executar_cobranca, mostrar_placar, verificar_fim_antecipado, escolher_modo)

def main():
    gol = criar_gol()

    print('==========================')
    print('       FIAPENALTYS')
    print('==========================')

    modo = escolher_modo()

    time_1 = input('Digite o nome do Time 1: ')
    time_2 = input('Digite o nome do Time 2: ')

    # CONTROLADORES PRINCIPAIS E INICIAIS
    controle_time_1 = 'JOGADOR'

    if modo == 1:
        controle_time_2 = 'JOGADOR'
    else:
        controle_time_2 = 'BOT'

    gols_time_1 = 0
    gols_time_2 = 0

    historico_time_1 = ['-', '-', '-', '-', '-']
    historico_time_2 = ['-', '-', '-', '-', '-']

    #JOGO PRINCIPAL
    for rodada in range(1, 6):
        os.system('cls')

        print(f'\n========== RODADA {rodada} DE 5 ==========')
        mostrar_placar(
            time_1, ''.join(historico_time_1),
            time_2, ''.join(historico_time_2)
        )

        #COBRANÇA DO TIME 1
        resultado = executar_cobranca(gol, time_1, time_2, controle_time_1, controle_time_2)

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
        resultado = executar_cobranca(gol, time_2, time_1, controle_time_2, controle_time_1)

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
            resultado = executar_cobranca(gol, time_1, time_2, controle_time_1, controle_time_2)

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
            resultado = executar_cobranca(gol, time_2, time_1, controle_time_2, controle_time_1)
            
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