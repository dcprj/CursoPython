from random import randint

print("*******************************")
print("Bem vindo ao jogo de advinhação")
print("*******************************")

numero_secreto = randint(1, 100)

chute = -1
tentativas = 0

while (True):
    chute = int(input("Digite o seu numero (0 para sair): "))
    print("Você digitou: ", chute)
    if (chute == 0):
        print("Você desistiu!")
        break
    tentativas += 1
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    if (acertou):
        print("*************************************************************")
        print(f'Você acertou em {tentativas} tentativa(s). Parabéns')
        print("*************************************************************")
    elif (maior):
        print("Você errou. Seu chute foi pra cima")
    else:
        print("Você errou. Seu chute foi pra baixo")
print("Fim do Jogo")