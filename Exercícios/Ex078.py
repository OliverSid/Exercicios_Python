'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

lista_cinco = []

for contagem in range(0,5):
    lista_cinco.append(int(input(f'Digite um número na posição {contagem}: ')))

print(f'Você digitou os valores: {lista_cinco}')
print('=-' * 40)
print(f'O maior valor digitado foi {max(lista_cinco)} na posição: ', end= '')
for i, v in enumerate(lista_cinco):
    if v == max(lista_cinco):
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {min(lista_cinco)} na posição: ', end= '')
for i, v in enumerate(lista_cinco):
    if v == min(lista_cinco):
        print(f'{i}... ', end='')
print()
