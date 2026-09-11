# 🥅 FIAPenaltys

FIAPenaltys é um jogo de disputa de pênaltis desenvolvido em Python para execução no terminal. O projeto utiliza funções, listas e uma matriz para representar o gol e calcular as chances de defesa.

## Como funciona

O gol é representado por uma matriz de 5 linhas e 8 colunas. Em cada cobrança, o batedor escolhe onde chutar e o goleiro escolhe onde defender.

A posição escolhida pelo goleiro preenche a matriz com diferentes chances de defesa:

- mesma posição do chute: 100%;
- posições próximas: 80%;
- posições mais distantes: 40%;
- fora do alcance: 0%.

Depois, o programa realiza um sorteio para definir se a cobrança terminou em gol ou defesa.

## Modos de jogo

- **Jogador contra jogador:** duas pessoas alternam entre cobrar e defender.
- **Jogador contra bot:** o jogador controla o primeiro time e o computador controla o segundo.

Cada time pode realizar até cinco cobranças. A partida termina antecipadamente quando um dos times não consegue mais alcançar o outro. Se houver empate após as cobranças iniciais, o jogo continua em rodadas alternadas até existir um vencedor.

## Como executar

É necessário ter o Python 3 instalado. No terminal, dentro da pasta do projeto, execute:

```bash
python main.py
```

## Estrutura do projeto

- `main.py`: controla as rodadas, o placar e os modos de jogo;
- `sistema_jogo.py`: contém as escolhas, confirmações, sorteios e regras da partida;
- `gol.py`: cria, exibe, limpa e calcula as chances na matriz do gol.

## Equipe

- Alexandre Salcines Messias Pivatti
- Gustavo Henrique Jardim de Sá
- Guilherme Boerato Medina
