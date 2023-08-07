''' Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''

def contador():
    print('-' * 30)
    print('Contagem de 1 até 10:')
    for c in range(1,11):
        print(f'{c}', end=' ')
    print('FIM')
    print('-' * 30)
    print('Contagem de 10 até 0 de 2 em 2:')
    for c in range (10, -1, -2):
        print(f'{c}', end= ' ')
    print('FIM')
    print('-' * 30)
    i = int(input('Agora é sua vez de personalizar a contagem.\nInicio: '))
    f = int(input('Fim: '))
    p = int(input('Pulo: '))
    while p == 0:
        p = int(input('ERRO! Não da pra pular de 0 em 0.\nPulo: '))
    for c in range(i,f,p):
        print(f'{c}', end=' ')
    print('FIM')


#programa principal
contador()
