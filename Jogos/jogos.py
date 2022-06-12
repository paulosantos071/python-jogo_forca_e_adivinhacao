import forca
import adivinhacao as adivinhacao

def escolher_jogo() :
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************\n")

    print("(1) - FORCA\n"
          "(2) - ADIVINHAÇÃO")

    jogo = int(input("Qual Jogos? "))

    if (jogo == 1):
        print("\nJogando forca...")
        forca.jogar()
    elif (jogo == 2):
        print("\nJogando adivinhação...")
        adivinhacao.jogar()

if __name__ == "__main__" :
    escolher_jogo()