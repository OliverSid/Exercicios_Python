#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
contador = soma = maior = menor = 0
escolha = "S"

while escolha in 'Ss':
    num = int(input('Digite um numero: '))
    escolha = str(input('Voce quer continuar? [S/N] ')).strip().upper()
    contador += 1
    soma += num
    if contador == 1:
        maior = menor = num
    if num < menor:
        menor = num
    if num > maior:
        maior = num

    if escolha == 'Nn':
        break
print(f'A media dos numeros que voce digitou é {soma/contador:.2f}, o menor numero digitado é {menor} e o maior numero digitado é {maior}.')
