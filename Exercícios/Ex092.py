'''Crie um programa que leia nome,
ano de nascimento e carteira de trabalho
e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação
e o salário. Calcule e acrescente, além da idade,
com quantos anos a pessoa vai se aposentar.'''

from datetime import datetime
ano = datetime.now()
cadastro = {}
cadastro['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
cadastro['Idade'] = ano.year - nascimento
cadastro['Ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if cadastro['Ctps'] != 0:
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salario'] = float(input('Salario: R$'))
    cadastro['Aposentadoria'] = (cadastro['Contratação'] - nascimento) + 35
print('-=' * 30)
for k, v in cadastro.items():
    print(f'- {k} tem o valor {v}.')
