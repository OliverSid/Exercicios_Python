#Crie um programa que leia dois valores e mostre um menu como o ao lado: Seu programa deverá realizar a operação solicitada em cada caso. 1 - somar, 2 - multiplicar 3 - maior, 4 - novos números, 5 sair 
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
soma = num1 + num2
vezes = num1 * num2

print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')

options = int(input('Qual a sua opção?\n'))

while options != 5: #se a opção for diferente de 5, irá realizar as opções erradas.
    if options == 1:
        print(f'A soma entre {num1} + {num2} = {soma}.')

    elif options == 2:
        print(f'A multiplicação entre {num1} x {num2} = {vezes}.')

    elif options == 3:
        if num1 > num2:
            print(f'Entre {num1} e {num2} o maior valor é {num1}.')
        elif num2 > num1:
            print(f'Entre {num1} e {num2} o maior valor é {num2}.')
        else:
            print(f'{num1} e {num2} tem o mesmo valor.')

    elif options == 4:
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Digite outro valor: '))
        
    elif options != range (1,5):
        print('Opção invalida.')

    print('=-'* 20 )
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n')
    options = int(input('Qual sua opção?\n'))

print('Tchau, espero te ver novamente!')
