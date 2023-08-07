'''Crie um programa que tenha uma função fatorial()
que receba dois parâmetros: o primeiro que indique
o número a calcular e outro chamado show, que será
um valor lógico (opcional) indicando se será mostrado
ou não na tela o processo de cálculo do fatorial.'''

def fatorial(num, show = False):
    """
    → Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return O valor fatorial de um número n.
    """
    if num == 0 or num == 1:
        return 1
    else:
        resultado = 1
        for n in range (num, 0, -1):
            if show:
                print(n, end = '')
                if n > 1:
                    print(' x ', end = '')
                else:
                    print(' = ', end = '')
            resultado *= n
        return resultado


#Programa Principal    
print(fatorial(5, show = True))
