#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('Digite um numero e lhe mostrarei sua tabuada: '))
    if num < 0:
        break
    for multiplicar in range (1,11):
        resultado = multiplicar * num
        print(f'{num} x {multiplicar:2} = {resultado}')
print('Obrigado por ter usado este programa.')
