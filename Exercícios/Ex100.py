'''Faça um programa que tenha uma lista
chamada números e duas funções chamadas
sorteia() e somaPar(). A primeira função
vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função vai
mostrar a soma entre todos os valores
pares sorteados pela função anterior.'''

from random import randint

numeros = []

def sorteia(list):
    contador = 1
    while contador <= 5:
        list.append(randint(0,10))
        contador += 1
    print(f'Sorteando os 5 valores: {list}')


def somaPar(list):
    soma = 0
    possui_par = False
    for num in list:
        if num % 2 == 0:
            soma += num
            possui_par = True
    if possui_par == True:
        print(f'A soma dos números pares dá lista é {soma}.')
    else:
        print('Não foram sorteados números pares.')
        
    
#Programa principal
sorteia(numeros)
somaPar(numeros)
