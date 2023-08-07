'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

soma_par = soma_coluna = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}, {coluna}]: '))

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
    print()

print ('-=' * 30)
print(f'A soma de todos os valores pares é {soma_par}')
for linha in range(0, 3):
    soma_coluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {soma_coluna}')
print(f'O maior valor da segunda coluna é {max(matriz[1])}')
