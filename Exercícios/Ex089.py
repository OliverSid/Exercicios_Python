'''Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta. No final,
mostre um boletim contendo a média de cada um
e permita que o usuário possa mostrar as notas
de cada aluno individualmente.'''

cadastro = []

while True:
    nome = str(input('Nome do aluno: ')).capitalize()
    nota1 = float(input('Digite a 1º nota: '))
    nota2 = float(input('Digite a 2º nota: ')) 
    media = (nota1 + nota2) / 2
    cadastro.append([nome,[nota1, nota2], media])

    resposta = str(input('Você quer continuar [S/N]?\n')).upper()

    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Comando incorreto.\nVocê quer continuar [S/N]?\n')).upper()
    
    if resposta == 'S':
        pass
    elif resposta == 'N':
        break

print('-=' * 20)
print(f'{"No":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 23)
for i, aluno in enumerate(cadastro):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8}')

while True:
    print('-' * 30)
    escolhido = int(input('Mostrar a nota de qual aluno?(999 interrompe): '))
    if escolhido == 999:
        print('FINALIZANDO...')
        break

    if escolhido <= len(cadastro) - 1:
        print(f'As notas de {cadastro[escolhido][0]} são {cadastro[escolhido][1]}')

print('Volte sempre.')
