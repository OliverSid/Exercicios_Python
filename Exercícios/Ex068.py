# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
from random import randint

print('Vamos jogar Par ou Impar.')
vitoria = 0 
while True:
    computador = randint(0,10)
    num = int(input('Digite um numero: '))
    escolha = str(input('Escolha entre Par ou Impar [P/I]: ')).strip().upper()
    soma = num + computador
    divisão  = (soma % 2)

    if escolha != "P" and escolha != "I":
        print('Não entendi sua escolha.\nDigite novamente.')
        num = int(input('Digite um numero: '))
        escolha = str(input('Escolha entre Par ou Impar [P/I]: ')).strip().upper()
        soma = num + computador
        divisão  = (soma % 2)


    if escolha == "P" and divisão == 0:
        print(f'Você ganhou!\nSua escolha foi {num} e a minha {computador}, a soma é {soma} que é Par.')
        vitoria += 1

    elif escolha == "P" and divisão != 0:
        print(f'Você perdeu!\nSua escolha foi {num} e a minha {computador}, a soma é {soma} que é Impar.')
        break

    if escolha == "I" and divisão != 0:
        print(f'Você ganhou!\nSua escolha foi {num} e a minha {computador}, a soma é {soma} que é Impar.')
        vitoria += 1

    elif escolha == "I" and divisão == 0:
        print(f'Você perdeu!\nSua escolha foi {num} e a minha {computador}, a soma é {soma} que é Par.')
        break

print(f'Obrigado por jogar, você venceu {vitoria} seguidas.')
