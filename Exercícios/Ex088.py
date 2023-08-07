'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 
6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from random import sample

jogos = []

quant_sorteio = int(input('Quantos sorteios você deseja fazer?\n'))

for jogo in range(quant_sorteio):
    palpites = sample(range(1, 60), 6)
    jogos.append(sorted(palpites))
    
    print(f'Jogo {jogo + 1}: {jogos[jogo]}')
    
jogos.clear()
