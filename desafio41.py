from datetime import datetime
ano = int(input('\033[34mInforme a sua data de nascimento\033[m: '))
data_atual = datetime.now().year
if data_atual - ano == 9:
    print('\033[31mMIRIM\033[m')
elif data_atual - ano == 14:
    print('\033[31mINFANTIL\033[m')
elif data_atual - ano == 19:
    print('\033[31mJUNIOR\033[m')
elif data_atual - ano == 20:
    print('\033[31mSÊNIOR\033[m')
else:
    print('\033[31mMASTER\033[m')