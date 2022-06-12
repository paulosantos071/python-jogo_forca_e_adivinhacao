print("*********************************")
print("Bem vindo ao jogo de adivinhacaio")
print("*********************************\n")

numero_secreto = 42



total_tentativas = 3
contador = 1

while contador <= total_tentativas:
    # A intrepolação de String de paiton é feito usando a função format()
    print("Tentaiva {} de {}".format(contador, total_tentativas))

    #  recebe como parâmetro uma string que será mostrada como auxílio ao usuário
    # precisa ser adicionado uma variavel para guardar essa entrada
    chute = int(input("Digite um numero: "))
    print("Você digitou ", chute)

    if numero_secreto == chute:
        print("você acertou!\n")
    else:
        if chute > numero_secreto:
            print('você errou, o seu chute foi maior que o numero secreto\n')
        # poderia utilizar o else aqui, mas essas é uma variação do elseif do java
        elif chute < numero_secreto:
            print("você errou, o seu chute foi menor que o numero secreto\n")
    # o python não suporta o ++ e nem o --
    contador+=1


print("Fim do jogo")
