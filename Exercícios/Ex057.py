#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" iu "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Qual seu sexo [M/F]?\n')).upper().strip()
while sexo != 'M' and sexo != 'F':  
#se a pessoa não digitar M ou F o programa irá pedir que ela digite novamente.
    print('Informação invalida, digite novamente.')
    sexo = str(input('Qual seu sexo [M/F]?\n')).upper().strip()
if sexo == 'M' or sexo == 'F':
    print('Sexo registrado com sucesso.')
