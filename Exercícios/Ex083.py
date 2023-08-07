'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
exprecao = str(input('Digite a expressão: '))
pilha = []
for simbolo in exprecao:
    if simbolo == '(':
        pilha.append('(')

    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()

        else:
            pilha.append(')')
            break    

if len(pilha) == 0:
    print('Sua expressão está valida.')
else:
    print('Sua expressão está invalida.')
