'''Crie um programa onde 4 jogadores joguem um dado
e tenham resultados aleatórios. Guarde esses resultados
em um dicionário em Python. No final, coloque esse
dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
ranking = ()

for dado in range (1,5):
    jogo[f'Jogador{dado}'] = randint(1,6)

for jogador, num in jogo.items():
    print(f'{jogador} tirou {num} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-' * 30)
print('Ranking')
for lugar, jogador in enumerate(ranking):
    print(f'{lugar + 1} lugar: {jogador[0]} com {jogador[1]}.')
