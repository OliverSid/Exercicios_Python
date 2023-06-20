# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('Vamos criar 10 termos de uma P.A.')

termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
contador = 1

while contador <= 10:
    print(f'{termo} ', end=' → ' )
    termo += razao
    contador += 1
print('ACABOU')
