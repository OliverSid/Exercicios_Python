'''Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de
uma pessoa, retornando um valor literal indicando
se uma pessoa tem voto NEGADO,
OPCIONAL e OBRIGATÓRIO nas eleições.''' 

def voto(nasc = 0):
    """
    Com o parâmetro 'nasc', é feito um calculo com o ano atual,
    que foi importado da biblioteca datetime, para ver se a 
    pessoa tem voto opcional, obrigatório ou Não vota.
    """
    from datetime import date
    atual = date.today().year
    v = atual - nasc
    if v >= 16 and v < 18 or v >= 70:
        return (f' Com {v} anos: VOTO OPCIONAL.')
    elif v >= 18 and v < 70:
        return (f'Com {v} anos: VOTO OBRIGATÓRIO.')
    else:
        return (f'Com {v} anos: NÃO VOTA.')


#Programa Principal
print('-' * 50)
ano = int(input('Digite seu ano de nascimento: '))
print(voto(ano))
