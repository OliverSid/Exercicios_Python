# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
numdigi = soma = 0
while True:
    num = int(input('Digite um numero[sabendo que ao digitar 999 o programa será parado]: '))
    if num == 999:
        break
    numdigi += 1
    soma += num
    
print(f'Foram digitados {numdigi} numeros e a soma entre eles é {soma}.')
