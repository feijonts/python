from random import randint

print("vamos jogar batalha naval")

jogo = True

tabuleiro = []
linhas =5
colunas=5

linha = ["O"] * colunas

for x in range(colunas):
    tabuleiro.append(["0"] * colunas)

navio_linha = randint(4,linhas-1)
navio_coluna = randint(4,colunas-1)

def mostra_tabuleiro(t):
    for L in t:
        print(" ".join(L))
        
while jogo:
    mostra_tabuleiro(tabuleiro)
    chute_linha = int(input("qual linha?"))-1
    chute_coluna = int(input("qual coluna?"))-1

    if chute_linha == navio_linha and chute_coluna == navio_coluna:
        print("Parabéns! Você acertou!!")
        jogo = False
    elif chute_linha >= linhas or chute_coluna >= colunas:
        print("Você chutou fora do tabuleiro")
    elif tabuleiro[chute_linha][chute_coluna] == "x":
        print("você já chutou aí")
    else:
        tabuleiro[chute_linha][chute_coluna] = "x"
