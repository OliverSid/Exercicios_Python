'''Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer
qual deles é o maior.
'''
from time import sleep

def maior(* numeros):
    print('-' * 50)
    print('Analisando os valores...')
    for n in numeros:
        print(n, end=' ')
        sleep(0.5)
    if len(numeros) > 0:
        print(f'\nForam informados {len(numeros)} números ao todo.')
        print(f'O maior deles foi {max(numeros)}.')
    else:
        print('Não foi passado nenhum valor.')


maior(5, 2, 1, 9, 3,)
maior(3, 6, 4, 7)
maior(1, 2)
maior(8)
maior()


