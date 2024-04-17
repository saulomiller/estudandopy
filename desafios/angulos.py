from math import radians, sin, cos, tan

ang = float(input('Digite o ângulo qualquer:'))

seno = sin (radians(ang))
print('O angulo de {} tem o Sen de {:.3f}'.format(ang, seno))

coss = cos (radians(ang))
print('O angulo de {} tem o Cos de {:.3f}'.format(ang, coss))

tg = tan (radians(ang))
print('O angulo de {} tem o Tan de {:.3f}'.format(ang, tg))
           