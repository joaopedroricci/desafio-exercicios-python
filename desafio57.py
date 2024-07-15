sexo = str(input('Informe seu sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido. Por favor, informe seu gênero: '))
print('Dado registrado com sucesso!')


