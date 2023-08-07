''' Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.'''

num_cadastrados = list()
contagem = 0

for valores in range(0,5):
    num = int(input('Digite um valor: '))

    if valores == 0 or num > num_cadastrados[-1]:
        num_cadastrados.append(num)
    else:
        posicao = 0
        while posicao <= len(num_cadastrados):
            if num <= num_cadastrados[posicao]:
                num_cadastrados.insert(posicao, num)
                break
print(f'Os números cadastrados em ordem crescente são {num_cadastrados}.')
