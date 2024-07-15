from time import sleep
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
opcao = 0
while opcao != 5:
    print('''
    [ 1 ] somar 
    [ 2 ] multiplicar 
    [ 3 ] maior 
    [ 4 ] novos número
    [ 5 ] sair do programa
    ''')
    opcao = int(input('Qual a sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print(' A soma entre {} + {} é {}.'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é:{}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os valores novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamnte.')
    print('=-=' * 10)
    sleep(2)
sleep(1)
print('fim do programa! volte sempre.')

