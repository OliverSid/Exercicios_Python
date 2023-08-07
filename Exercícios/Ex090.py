'''Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''
aluno = {}

aluno['Nome'] = str(input('Digite o nome do estudante: ')).capitalize().strip()
aluno['Média'] = float(input('Digite a média do estudante: '))
if aluno['Média'] < 7:
    aluno['Situação'] = 'Reprovado'
else:
    aluno['Situação'] = 'Aprovado'

print('-' * 30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}.')
