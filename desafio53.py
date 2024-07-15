frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letras in range(len(junto)-1, -1, -1):
    inverso += junto[letras]
print('Inverso de {} è {}.'.format(junto, inverso))
if inverso == junto:
    print('A frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')

