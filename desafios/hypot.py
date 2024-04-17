from math import hypot
co = float(input('comprimento do cateto oposto:'))
ca = float(input('comprimento do cateto adejacente:'))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.3f}'.format(hi))


###pode usar o modulo inteiro de matematica import math

### sem o modulo math
#OPS = float(input('catOPS:'))
#ADJ = float(input('catADJ:'))
#hp = (OPS ** 2 + ADJ ** 2) ** (1/2)
#print('A hipotenusa mede: {}'.format(hp))          
           