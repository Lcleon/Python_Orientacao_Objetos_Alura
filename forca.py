def jogar():
    print("********************************")
    print("***Bem vindo ao jogo da forca***")
    print("********************************")

    palavra_secreta = "futebol".upper()

    enforcado = False
    acertou = False

    print(f"Olá, eu sou o PC e minha palavra secreta tem {len(palavra_secreta)} letras. ")
    print("Tente acertar.")

    while (not enforcado and not acertou):
        chute = input("Qual letra?").upper()
        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                print(f"Encontrei a letra {letra} na posição {index + 1}")
            index += 1

        print("Jogando...")

    print("Fim de jogo")


if (__name__ == "__main__"):
    jogar()
