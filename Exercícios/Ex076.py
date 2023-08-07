'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

tabela = ('Lápis', 1.75, 'Borracha', 2.0, 'Caderno', 15.90, 'Estojo', 25.90, 'Mochila', 120.0)

titulo = 'LISTAGEM DE PREÇOS'
print("--" * 20)             
print(f"{titulo: ^40}")
print("--" * 20)     
for items in tabela:       
    if type(items) == str:
        print(f"{items:.<30}", end="")
    if type(items) == float:
        print(f"R${items: >7.2f}")
print("--" * 20)
