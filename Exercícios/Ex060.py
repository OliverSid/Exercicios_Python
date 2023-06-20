#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#from math import factorial

#num = int(input('Digite um numero: '))

##print(f'O fatorial de {num} é {factorial(num)}')

num = int(input('Digite um numero: '))
fatorial = 1
i = 1

while i <= num:
    fatorial = fatorial * i
    i = i + 1

print(f'O fatorial de {num} é {fatorial}')
