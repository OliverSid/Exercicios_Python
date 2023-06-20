#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
contador = num = soma = 0
while num != 999:
    num = int(input('Digite um valor quantas vezes quiser aqui e quando você digitar o numero 999 vamos parar: '))
    soma += num
    contador += 1
    
print(f'Você digitou {contador - 1} numeros, a soma entre eles é {soma - 999}')
