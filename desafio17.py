import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
h1 = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}' .format(h1))
