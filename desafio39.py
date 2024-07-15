from datetime import datetime
sexo = str(input('Informe seu gênero: '))
data_atual = int(input('\033[31mInforme seu ano de nascimento\033[m: '))
ano_atual = datetime.now().year
soma1 = 18 - (ano_atual - data_atual)
soma2 = (ano_atual - data_atual) - 18
if sexo == 'mulher':
    print('alistamento não abrigatorio')
elif (ano_atual - data_atual) < 18:
    print('\033[36mVocê ainda terá que se alistar\033[m')
    print('\033[36mfalta um total de {} anos para você prestar seu alistamento.\033[m' .format(soma1))
elif (ano_atual - data_atual) == 18:
    print('\033[36mVocê já pode se alistar\033[m')
elif (ano_atual - data_atual) > 18:
    print('\033[36mVocê já passou do tempo de se alistar\033[m')
    print('\033[36mvocê está atrasado um total de {} anos\033[m'.format(soma2))


