while True:
    tabuada = int(input('Qual tabuada você quer ver: '))
    if tabuada < 0:
        break
    print('-'*30)
    for c in range(1, 11):
        print(f'{tabuada} X {c} = {tabuada * c}')
    print('-'*30)
print('Fim da tabuada!')



