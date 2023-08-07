'''Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.'''
def area(largura,comprimento):
    a = largura * comprimento
    print(f'A area do terreno {largura} x {comprimento} é de {a}m².')


#Programa Principal
print('     CONTROLE DE TERRENOS')
print('-' * 30)
area(largura = float(input('largura: ')), comprimento = float(input('Comprimento: ')))
