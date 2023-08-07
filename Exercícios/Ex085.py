'''Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores pares
 e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

num_cadastrados = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}º numero: '))
    if valor % 2 == 0:
        num_cadastrados[0].append(valor)
    else:
        num_cadastrados[1].append(valor)
print(f'Os valores pares cadastrados são {sorted(num_cadastrados[0])} e os valores impares são {sorted(num_cadastrados[1])}.')
