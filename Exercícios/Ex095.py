'''Aprimore o desafio 93 para que ele funcione
com vários jogadores, incluindo um sistema de
visualização de detalhes do aproveitamento de cada jogador.
'''
jogadores = []
jogador = {}
gol = []
while True:
    jogador.clear()
    gol.clear()
    jogador['nome'] = str(input('Qual o nome do jogador?\n')).capitalize()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} Jogou: '))
    for g in range(partidas):
        gol.append(int(input(f'Quantos gols na partida {g + 1}: ')))
        jogador['gols'] = gol.copy()
    jogador['total'] = sum(gol)
    jogadores.append(jogador.copy())
    
    continuar = str(input('Quer continuar? [S/N]\n')).upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('ERRO! Você quer continuar? [S/N]'))
    if continuar == 'N':
        break

print('-=-' * 25)
print(f'{"Cod":>3} {"Nome":<14} {"Gols":<14} {"Total":<6} ')
print('-' * 50)
for c, n in enumerate(jogadores):
    print(f'{c:>3} {n["nome"]:<14} {str(n["gols"]):<14} {str(n["total"]):<6}')
print('-=-' * 25)
while True:
    cod = int(input('Mostrar dados de qual jogador digitando seu código(999 interrompe): '))
    if cod == 999:
        print('FINALIZANDO...')
        break
    
    elif cod <= len(jogadores) - 1:
        print(f'--- Levantamento do jogador {jogadores[cod]["nome"]}:')
        for k, v in enumerate(jogadores[cod]['gols']):
            print(f'    No jogo {k + 1} fez {v} gol(s).')
print('Volte Sempre.')
