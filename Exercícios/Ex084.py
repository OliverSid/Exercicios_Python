''' Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

cadastro_temp = []
cadastro = []
maior = menor = 0



while True:
    cadastro_temp.append(str(input('Digite seu nome: ')))
    cadastro_temp.append(float(input('Digite seu peso: ')))
    if len(cadastro) == 0:
        maior = menor = cadastro_temp[1]
    else:
        if cadastro_temp[1] > maior:
            maior = cadastro_temp[1]
        if cadastro_temp[1] < menor:
            menor = cadastro_temp[1]

    cadastro.append(cadastro_temp[:])
    cadastro_temp.clear()

    resposta = str(input('Voce quer continuar cadastrando pessoas?[S/N]\n')).upper()
    
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Comando incorreto.\nVoce quer continuar?[S/N]\n')).upper()
    
    if resposta == 'S':
        pass
    elif resposta == 'N':
        break

print('=-=' * 30)
print(f'Ao todo foram cadastradas {len(cadastro)} pessoas.')
print(f'O menor peso foi {menor}Kg.', end= '')
for p in cadastro:
    if p[1] == menor:
        print(f'[{p[0]}]', end= '')
print()
print(f'O maior peso foi {maior}Kg.', end= '')
for p in cadastro:
    if p[1] == maior:
        print(f'[{p[0]}]', end= '')
print()
