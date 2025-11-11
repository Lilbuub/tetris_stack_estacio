"""jogo bem simples de tetris stack, quis utilizar apenas import
random e import time que são bem simples"""

import random
import time

largura = 6
altura = 8

# cria o tabuleiro vazio
tabuleiro = []
for i in range(altura):
    linha = [" "] * largura
    tabuleiro.append(linha)

while True:
    coluna = random.randint(0, largura - 1)
    linha = 0

    # faz a peça cair
    while linha < altura - 1 and tabuleiro[linha + 1][coluna] == " ":
        linha = linha + 1
        time.sleep(0.1)

    # coloca a peça no tabuleiro
    tabuleiro[linha][coluna] = "█"

    # mostra o tabuleiro na tela
    for l in tabuleiro:
        print("".join(l))
    print("-" * largura)

    time.sleep(0.3)