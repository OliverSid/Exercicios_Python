''' Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

num_cadastrados = []
num_pares = []
continuar = True

while True:
    num_cadastrados.append(int(input('Digite um número: ')))

    resposta = str(input('Você quer continuar? [S/N]\n')).upper()

    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Comando incorreto. Deseja continuar? [S/N]\n')).upper()

    if resposta == 'S':
        pass
    
    elif resposta == 'N':
        continuar = False
        break

print(f'Foram digitados {len(num_cadastrados)} números.')

num_cadastrados.sort(reverse=True)
print(f'A lista na ordem decrescente é {num_cadastrados}')

if 5 in num_cadastrados:
    print(f'O valor 5 foi digitado e está na lista: {num_cadastrados}.')
else:
    print(f'O valor 5 não foi digitado na lista: {num_cadastrados}.')
