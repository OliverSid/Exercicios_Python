#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
#Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

print('Vamos fazer uma sequencia de Fibonacci.')

n = int(input('Digite um numero: '))
fibo1 = 0 #numero para a sequencia Fibonacci
fibo2 = 1 #outro numero para a sequencia Fibonacci

contagem = 3

print(f'{fibo1} → {fibo2}', end= " → ")

while contagem <= n:
    fibo3 = fibo1 + fibo2
    print(f'{fibo3}', end= " → ")
    contagem += 1
    fibo1 = fibo2
    fibo2 = fibo3

print('FIM.')
