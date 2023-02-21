from random import randint as ri

def jogar():
    print("********************************")
    print("***Bem vindo ao jogo da advinhação**")
    print("********************************")

    m = ri(1, 10)
    level_1 = 10
    level_2 = 5
    level_3 = 3
    s_level = int(input("Qual nível deseja jogar: Easy[1] - Medium[2] - Hard[3] ?"))
    if (s_level == 1):
        s_level = level_1
    elif (s_level == 2):
        s_level = level_2
    else:
        s_level = level_3

    print(f"N° da máquina = {m}")

    for i in range(s_level):
        n = int(input(f"Digite o seu número: "))
        if (n < 1 or n > 10):
            print("Dígito inválido!")
            continue
        ac = n == m
        mi = n > m
        me = n < m

        if (ac):
            print("Acertou!!!")
            print(f"Jogador  -> {n} | computador -> {m}")
            break
        else:
            if (mi):
                print("Jogador [+] x [-] Computador")
            elif (me):
                print("Jogador[-] x [+] Computador")

    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()