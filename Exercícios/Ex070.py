#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
'''A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

valortotal = mais_qmil = valor_produto_barato = cont_produto = 0
nome_produto_barato = ""

while True:
    produto = str(input('Qual o nome do produto?\n')).strip().title()
    valor = float(input('Qual o preço do produto R$:'))
    continuar = str(input('Você gostaria de continuar [S/N]: ')).strip().upper()
    valortotal += valor
    cont_produto += 1

    if cont_produto == 1:
        valor_produto_barato = valor
        nome_produto_barato = produto
    else:
        if valor < valor_produto_barato:
            valor_produto_barato = valor
            nome_produto_barato = produto

    if valor > 1000:
        mais_qmil +=1
    
    while continuar != "S" and continuar != 'N':
        print('Não entendi sua escolha. Tente novamente sabendo que "S" é para sim e "N" para não.')
        continuar = str(input('Você gostaria de continuar [S/N]: ')).strip().upper()
    if continuar == "S":
        print('Você decidiu continuar comprando.')
        pass
    
    if continuar == "N":
        print('Você está encerrando as compras.')
        break

print(f'O total de sua compra foi R${valortotal:.2f}')
print(f'Foram comprados {mais_qmil} produtos que valem mais de R$1000.00')
print(f'O nome do produto mais barato é {nome_produto_barato} e seu valor foi de R${valor_produto_barato:.2f}.')
