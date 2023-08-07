'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ('Livro', 'Carteira', 'Monitor', 'Fone', 'Programar', 'Cama')
vogais = ('a', 'e', 'i', 'o', 'u')

for palavra in palavras:
    print(f'Na Palavra ({palavra}):', end= ' ')

    for letra in palavra:
        if letra.lower() in vogais:
            print(f'{letra.lower()}', end= ' ')
    print()
