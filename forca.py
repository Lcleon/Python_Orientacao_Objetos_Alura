def jogar():
    print("********************************")
    print("***Bem vindo ao jogo da forca***")
    print("********************************")

    palavra_secreta = "FUTEBOL"
    palavras_acertadas = ["_","_","_","_","_","_","_"]

    enforcado = False
    acertou = False

    print(f"Olá, eu sou o PC e minha palavra secreta tem {len(palavra_secreta)} letras. ")
    print(palavras_acertadas)
    print("Tente acertar.")

    while (not enforcado and not acertou):
        chute = input("Qual letra?").upper().strip()
        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                palavras_acertadas[index] = letra
                letras_faltando = str(palavras_acertadas.count('_'))
                print(f"Ainda faltam {letras_faltando} letras")

            index += 1

        print(palavras_acertadas)

    print("Fim de jogo")


if (__name__ == "__main__"):
    jogar()
