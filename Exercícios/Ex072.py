#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

n_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
            'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
            'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
            'Quinze', 'Dezesseis', 'Dezessete',
            'Dezoito', 'Dezenove', 'Vinte')

continuar = True

while True: #loop infinito.
    numero_digitado = int(input('Digite um número entre 0 e 20: ')) 

    if numero_digitado not in range(0,21):# se o número digitado pelo usuário, não for de 1 até 20.
        print('O número digitado não está entre 0 e 20.', end=' ') 

    if numero_digitado in range(0,21): #se o número digitado estiver entre 0 e 20, será exibido ao usuário.
        print(f'Você digitou o número {n_extenso[numero_digitado]}.') #n_extenso é a tupla e o número digitado dentro de [] vai buscar o numero que equivale a ele.

    resposta = str(input('Deseja continuar? [S/N]\n')).upper()

    while resposta != 'N' and resposta != 'S':
        resposta = str(input('Resposta invalida. Deseja continuar? [S/N]\n')).upper()
    
    if resposta == 'N':
        continuar = False
        break
print('Agradeço por você ter usado o programa. Até mais!')
