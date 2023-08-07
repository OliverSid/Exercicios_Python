'''Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

numeros_cadastrados = []
cadastrados_par = []
cadastrados_impar = []
continuar = True 

while True:
    num = int(input('Cadastre um número: '))
    numeros_cadastrados.append(num)

    if (num % 2) == 0:
        cadastrados_par.append(num)

    else:
        cadastrados_impar.append(num)

    resposta = str(input('Você quer continuar?[S/N]\n')).upper()

    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Comando incorreto.\nVocê quer continuar?[S/N]\n')).upper()
    
    if resposta == 'S':
        pass

    if resposta == 'N':
        break

numeros_cadastrados.sort()
cadastrados_par.sort()
cadastrados_impar.sort()

print(f'Os números cadastrados foram {numeros_cadastrados}')
print(f'Os números cadastrados que são pares foram {cadastrados_par}')
print(f'Os números cadastrados que são impares foram {cadastrados_impar}')
