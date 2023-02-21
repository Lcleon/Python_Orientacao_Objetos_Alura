def jogar():
    print("********************************")
    print("***Bem vindo ao jogo da forca***")
    print("********************************")

    palavra_secreta = "carro"
    palavra_secreta = palavra_secreta.upper()

    enforcado = False
    acertou = False

    print(f"Olá, eu sou o PC e minha palavra secreta tem {len(palavra_secreta)} letras. ")
    print("Tente acertar.")

    while (True):
        chute = input("Qual letra?")
        chute = chute.upper()
        for letra in palavra_secreta:
            if(chute == letra):
                print(chute)


        print("Jogando...")
    print("Fim de jogo")

if (__name__ == "__main__"):
    jogar()
