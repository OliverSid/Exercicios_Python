#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('==' * 25)
print('Bem vindo, Você está acessando o Caixa Eletrônico.')
print('==' * 25)

saque = int(input('Qual é o valor que você quer sacar R$:'))
cedula_cinq = cedula_vinte = cedula_dez = cedula_um = 0 #contador de cedulas

while True:
    while saque - 50 >= 0: #Se o saque for maior ou igual a 50, será descontado 50 do saque e adicionado 1 na variável cedula_cinq
        saque -= 50 
        cedula_cinq += 1

    while saque - 20 >= 0: #Se o saque for maior ou igual a 20, será descontado 20 do saque e adicionado 1 na variável cedula_vinte
        saque -= 20
        cedula_vinte += 1

    while saque - 10 >= 0: #Se o saque for maior ou igual a 10, será descontado 10 do saque e adicionado 1 na variável cedula_dez
        saque -= 10
        cedula_dez += 1

    while saque - 1 >= 0: #Se o saque for maior ou igual a 1, será descontado 1 do saque e adicionado 1 na variável cedula_um
        saque -= 1
        cedula_um += 1

    break

if cedula_cinq != 0: #Se a variável de cedula_cinq for diferente de 0, será exibido a quantidade de cedulas de 50 sacadas.
    print(f'Foram sacadas {cedula_cinq} cedulas de R$50.')

if cedula_vinte != 0: #Se a variável de cedula_vinte for diferente de 0, será exibido a quantidade de cedulas de 20 sacadas.
    print(f'Foram sacadas {cedula_vinte} cedulas de R$20.')

if cedula_dez != 0: #Se a variável de cedula_dez for diferente de 0, será exibido a quantidade de cedulas de 10 sacadas.
    print(f'Foram sacadas {cedula_dez} cedulas de R$10.')

if cedula_um != 0: #Se a variável de cedula_um for diferente de 0, será exibido a quantidade de cedulas de 1 sacadas.
    print(f'Foram sacadas {cedula_um} cedulas de R$1.')

print('==' * 25)
print('Volte sempre e tenha um ótimo dia.')
