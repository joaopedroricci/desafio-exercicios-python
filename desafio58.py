from random import randint
computador = randint(0, 10)
print('Sou seu computador e acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpite = 0
while not acertou:
    pessoa = int(input('Qual o seu palpite: '))
    palpite += 1
    if pessoa == computador:
        acertou = True
        palpite += 1
    else:
        if pessoa < computador:
            print('O computador pensou em um número maior, tente novamente.')
        elif pessoa > computador:
            print('O computador pensou em um número menor, tente novamente.')
print('Você acertou!')
print('Você acertou em {} tentativas'.format(palpite))





