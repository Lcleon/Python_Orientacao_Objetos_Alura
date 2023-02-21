import advinhacao
import forca
def jogar():
    print("Escolha o jogo:")
    print("[ 1 ] Advinhação [ 2 ] Jogo da forca")
    escolha = int(input("Digite a opção: "))

    if(escolha == 1):
        print("Jogo de advinhação")
        advinhacao.jogar()
    else:
        print("Jogo da forca")
        forca.jogar()

if(__name__ == "__main__"):
    jogar()



