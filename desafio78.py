listaNum = []
mai = 0
men = 0
for c in range(0, 5):
    listaNum.append(int(input(f'Digite um valor para posição {c}: ')))
    if c == 0:
        mai = men = listaNum[c]
    else:
        if listaNum[c] > mai:
            mai = listaNum[c]
        if listaNum[c] < men:
            men = listaNum[c]
print(f'você digitou os valores: {listaNum}')
print(f'O maior valor digitado foi {mai} nas posicões', end=' ')
for i, v in enumerate(listaNum):
    if v == mai:
        print(f'{i}...', end=' ')
print()
print(f'O menor valor digitado foi {men} nas posicões', end=' ')
for i, v in enumerate(listaNum):
    if v == men:
        print(f'{i}...', end=' ')
print()
