a = int(input('Informe a primeiro valor: '))
b = int(input('Informe o segundo valor: '))
c = int(input('Informe o terceiro valor: '))
# verificando o menor valor
menor = a
if b < a and b < c:
    manor = b
if c < a and c < b:
    menor = c
# verificando o maior valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi: {}' .format(menor))
print('O maior valor digitado foi: {}' .format(maior))


