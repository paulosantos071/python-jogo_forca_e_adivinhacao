import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhacaio")
    print("*********************************\n")

    # random.random() gera um numero entre 0.0 e 1.0
    # random.randrange() deve passar em paremetros o inicio e o fim
    numero_secreto = random.randrange(1, 101)
    total_tentativas = 3
    pontos = 100

    print("Qual nivel de dificuldade?\n "
          "(1) Facil\n (2) Médio\n (3) Dificil")

    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    # não faz a necessidade de criar uma variavel contador e ir incrementando ela, o for faz isso
    # cria uma variavel, e dentro do range fala o ponto de inicio e fim
    for contador in range(1, total_tentativas+1):

        print("Tentaiva {} de {}".format(contador, total_tentativas))
        chute = int(input("Digite um numero: "))
        print("Você digitou ", chute)

        # operadores logicos geralnmente são escritos (or, and, not)
        if (chute > 100 or chute < 1):
            print("Digite um valor entre 1 e 100")
            # o continue ele vai para a proxima iteração
            continue

        if (numero_secreto == chute):
            print("você acertou e fez {} pontos!\n".format(pontos))
            break
        else:
            if (chute > numero_secreto):
                print('você errou, o seu chute foi maior que o numero secreto\n')

            elif (chute < numero_secreto):
                print("você errou, o seu chute foi menor que o numero secreto\n")
            # abs é de numero absoluto
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos



    print("Fim do jogo")

if __name__ == "__main__" :
    jogar()

