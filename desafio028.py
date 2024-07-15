from random import randint
from time import sleep
computador = randint(0, 5)
print('Pensei em um número....')
jogador = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(5)
if jogador == computador:
    print('PARABENS VOCÊ ME VENCEU!')
else:
    print('VOCÊ ERROU EU PESSEI NO NÚMERO {} E NÃO NO {} '. format(computador, jogador))


