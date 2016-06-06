from random import randint

print "vamos jogar batalha naval"

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
        print " ".join(L)
        
while jogo:
    mostra_tabuleiro(tabuleiro)
    chute_linha = input("qual linha?")-1
    chute_coluna = input("qual coluna?")-1

    if chute_linha == navio_linha and chute_coluna == navio_coluna:
        print "Parab�ns! Voc� acertou!!"
        jogo = False
    elif chute_linha >= linhas or chute_coluna >= colunas:
        print "Voc� chutou fora do tabuleiro"
    elif tabuleiro[chute_linha][chute_coluna] == "x":
        print "voc� j� chutou a�"
    else:
        tabuleiro[chute_linha][chute_coluna] = "x"
