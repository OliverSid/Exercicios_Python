''' Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

tupla_valores = () #tupla vazia para receber os valores digitados
tupla_pares = () #tupla vazia para receber os valores que são pares
contagem = 0 #contagem para o while

while True:
    valores = int(input('Digite um numero de 0 a 10: ')) #Onde o usuário irá digitar o valor
    tupla_valores = tupla_valores + (valores,) #adicam dos valores a tupla
    contagem += 1 #contagem para encerrar o while.
    
    if valores % 2 == 0: #calculo para descobrir se o número é par
        tupla_pares = tupla_pares + (valores,) #adição dos números pares à tupla

    if contagem == 4: #contagem encerrada quando chegar no 4
        break

print(f'Os valores digitados foram: {tupla_valores}')

print(f'O número 9 apareceu {tupla_valores.count(9)} vez(es).') #count serve para contar quantas vezes algo entre as () apareceu, no caso o 9

if 3 in tupla_valores: 
    print(f'O numero 3 apareceu na {tupla_valores.index(3) + 1}ª posição.') #index serve para descobrir em que posição está o valor entre ()

else:
    print('O número 3 não foi digitado.')

print(f'O(s) número(s) par(es) digitado(s) é/são: {tupla_pares}')
