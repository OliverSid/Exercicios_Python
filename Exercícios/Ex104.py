'''Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante 'a função
input() do Python, só que fazendo a validação
para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')'''

def leiaInt(msg):
    n = str(input(f'{msg}'))
    if n.isnumeric():
        n = int(n)
        return n
    while n != n.isnumeric():
        n = str(input(f'ERRO! Digite um numero valido.\n{msg}'))
        if n.isnumeric():
            n = int(n)
            return n
    

#Programa Principal
n = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}.')
