cont = soma = 0
while True:
    numero = int(input('Informe um número: '))
    cont += 1
    if numero == 999:
        break
    soma += numero
print(f'Você digitou um total de {numero} e a soma entre eles é {soma}')
