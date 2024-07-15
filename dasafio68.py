from random import randint
v = 0
while True:
    jogador = int(input('Informe um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()
    print(f'Você jogou {jogador} e o computador jogou {computador}.', end='')
    print('Deu Par!' if total % 2 == 0 else 'Deu Ímpar!')
    if tipo == 'P':
        if total % 2 == 0:
            print('você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('você perdeu!')
            break
        print('Vamos jogar novamente!')
print(f'Você ganhou um total {v} vezes.')
