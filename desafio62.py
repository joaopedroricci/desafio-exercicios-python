print('gerador de PA')
print('-=-' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= 10:
        print('{} -> '.format(termo), end="")
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostras  a mais: '))
print('Fim')
