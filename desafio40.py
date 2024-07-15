nome = str(input('\033[31mDigite o nome do aluno:\033[m '))
nota1 = float(input('\033[31mInforme a primeira nota:\033[m '))
nota2 = float(input('\033[31mInforme a segunda nota:\033[m '))
media = (nota1 + nota2)/2
if media < 5.0:
    print('\033[34mREPROVADO!\033[m')
    print('\033[33mO aluno {} tirou média {} por tanto foi reprovado.\033[m' .format(nome, media))
elif media == 5.0 and 6.9:
    print('\033[34mRECUPERAÇÃO\033[m')
    print('\033[33mO aluno {} tirou média {} por tando  ficou em recuperação.\033[m'.format(nome, media))
elif media == 7.0 or media > 7.0:
    print('\033[34mAPROVADO\033[m')
    print('\033[33mO aluno {} tirou nota {} e foi aprovado.\033[m' .format(nome, media))
