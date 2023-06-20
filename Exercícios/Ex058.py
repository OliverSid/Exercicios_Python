#Melhore o Ex028 onde o computador vai "pensar" em um numero de 0 a 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint #biblioteca para randomizar

computador = randint (1, 11) #números que o computador ira escolher
print('Bem Vindo!')
print('Sou seu computador e quero saber se voce consegue adivinhar o numero que estou pensando.')
usuario = int(input('Digite um numero de 1 a 10: '))
contador = 0
while usuario != computador:
    if usuario > computador:
        usuario = int(input('Tente um numero menor: '))
        contador += 1
    
    elif usuario < computador:
        usuario = int(input('Tente um numero maior: '))
        contador += 1

print(f'\033[32mParabéns!\033[m O numero que eu pensei foi \033[33m{computador}\033[m, voce acertou em \033[31m{contador}\033[m tentativas.')
print('Foi um prazer jogar com você.')
