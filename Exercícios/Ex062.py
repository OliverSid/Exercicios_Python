# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('Gerador de PA.')

termo = int(input('Digite o termo: '))
razão = int(input('Digite a razão: '))
contador = 1

while contador <= 10:
    print(termo, end=' → ')
    termo += razão
    contador += 1
print('PAUSA.')

while True:
    novo_contador = int(input('Quantos termo você quer a mais?\n'))
    if novo_contador == 0:
        print(f'Progressão finalizada com {contador} termos mostrados.')
        break
    else:
        for pa in range(novo_contador):
            print(termo, end=' → ')
            termo += razão
            contador += 1
