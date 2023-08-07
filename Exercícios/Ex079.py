''' Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro,
ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente. '''

cadastro_num = []
continuar = True
while True:
    num = (int(input('Digite um número: ')))

    if num in cadastro_num:
        print(f'Esse número já foi cadastrado.\nNão será adicionado.')
        resposta = str(input('Você quer continuar? [S/N]\n')).upper()

    else:
        cadastro_num.append(num)
        print('Número cadastrado com sucesso...')
        resposta = str(input('Você quer continuar? [S/N]\n')).upper()

    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Comando invalido, Você quer continuar? [S/N]\n')).upper()

    if resposta == 'N':
        continuar = False
        break
    
print(f'Os números cadastrados foram {sorted(cadastro_num)}.')
