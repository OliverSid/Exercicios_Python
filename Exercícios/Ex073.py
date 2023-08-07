'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Inglês de Futebol, na ordem de colocação.
Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Brentford.'''

times = ('Arsenal', 'Manchester City', 'Manchester United', 'Tottenham Hotspur', 
        'Newcastle United', 'Liverpool', 'Brighton & Hove Albion', 'Brentford',
        'Fulham', 'Chelsea', 'Aston Villa', 'Crystal Palace', 'Wolverhampton Wanderers',
        'Leeds United', 'Everton', 'Nottingham Forest', 'Leicester City',
        'West Ham United', 'Bournemouth', 'Southampton')

print(f'A tabela do dia 28/03/23 é {times}')
print('=-' * 70)
print(f'Os primeiro cinco colocados são {times[:5]}')
print('=-' * 70)
print(f'Os 4 últimos times são {times[-4:]}')
print('=-' * 70)
print(f'Os times em ordem alfabética são {sorted(times)}')
print(f'=-' * 70)
print(f'O Brentford está em {times.index("Brentford") + 1}ª. ')

'''for colocados, times in enumerate(times):
    if colocados == 7:
        print(f'O time que está em {colocados + 1}ª é o {times}.')
        break'''
