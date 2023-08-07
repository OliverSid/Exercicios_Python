''' Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também
indique o menor e o maior valor que estão na tupla.'''

from random import randint #biblioteca para sortear os números

numeros_sorteados = (randint(1, 10), randint(1, 10), randint(1, 10),
                    randint(1, 10), randint(1, 10) ) 

print(numeros_sorteados)
print(f'O menor número é {min(numeros_sorteados)} e o maior é {max(numeros_sorteados)}.')