# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
'''A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.''' 
quantid = 0
quantm = 0
quantf = 0
while True:
    idade = int(input('Me informe a sua idade: '))
    sexo = str(input('Me informe o seu sexo [M/F]: ')).strip().upper()
    continuar = str(input('Você quer continuar [S/N]? ')).strip().upper()

    if idade >= 18:
        quantid += 1
    
    if sexo == 'M':
        quantm += 1
    
    if sexo == 'F':
        if idade < 20:
            quantf += 1
        
    if continuar == 'S':
        print('Você decidiu continuar a cadastrar pessoas.')
        pass

    if continuar != 'S' and continuar != 'N':
        print('Não entendi sua decisão, por favor usa apenas "S" para sim e "N" para não. ')
        continuar = str(input('Você quer continuar [S/N]? ')).strip().upper()
        if continuar == 'S':
            print('Você decidiu continuar a cadastrar pessoas.')
            pass

        if continuar == 'N':
            print('Você decidiu parar de cadastrar pessoas segue o relatório abaixo:')
            break
        
        if continuar != 'S' and continuar != 'N':
            print('Não entendi sua decisão, então vou encerrar o cadastramento de pessoas, segue abaixo o relatório:')
            break

    if continuar == 'N':
        print('Você decidiu parar de cadastrar pessoas segue o relatório abaixo:')
        break

print(f'Foram cadastradas {quantid} pessoas maiores de 18.')
print(f'Foram cadastrados {quantm} homens.')
print(f'Foram cadastradas {quantf} mulheres abaixo de 20 anos.')
