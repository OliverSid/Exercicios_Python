'''Crie um programa que gerencie o aproveitamento
de um jogador de futebol. O programa vai ler o nome
do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos
em cada partida. No final, tudo isso será guardado
em um dicionário, incluindo o total de gols feitos
durante o campeonato.'''

jogador = {}
gol = []
jogador['nome'] = str(input('Qual o nome do jogador?\n')).capitalize()
partidas = int(input(f'Quantas partidas {jogador["nome"]} Jogou: '))
for g in range(partidas):
    gol.append(int(input(f'Quantos gols na partida {g + 1}: ')))
    jogador['gols'] = gol
jogador['total'] = sum(gol)
print('-=-' * 25)
print(jogador)
print('-=-' * 25)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')
print('-=-' * 25)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, gols in enumerate(jogador['gols']):
    print(f'→ Na partida {i + 1}, fez {gols} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
