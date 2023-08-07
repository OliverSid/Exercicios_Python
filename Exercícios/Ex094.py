'''Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

dados = {}
cadastro = []
soma = media = 0

while True:
    dados['nome'] = str(input('Nome: ')).capitalize().strip()
    dados['sexo']= str(input('Sexo [M/F]: ')).upper()
    if dados['sexo'] != 'M' and dados['sexo'] != 'F':
        dados['sexo'] = str(input('ERRO! Por favor use [M/F]: ')).upper()
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    cadastro.append(dados.copy())
    continuar = str(input('Voce quer continuar [S/N]?\n')).upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('ERRO! Voce quer continuar [S/M]?\n')).upper()
    if continuar == 'N':
        break

media = soma / len(cadastro)
print('-=' * 30)
print(f'A) Ao todo temos {len(cadastro)} pessoas.')
print(f'B) A media de idade é {media:.2f}')
print('C) As mulheres cadastradas foram ', end='')
for p in cadastro:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end='')
        print()
print(f'D) Lista de pessoas que estão acima da media de idade:')
for p in cadastro:
    if p['idade'] > media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}', end='')
            print()
