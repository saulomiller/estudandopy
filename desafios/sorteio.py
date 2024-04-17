### sortea nomes listados
import random

n1 = str (input(('Digite um nome para ser sorteado:')))
n2 = str (input(('Digite mais um nome para ser sorteado:')))
n3 = str (input(('Digite mais um nome para ser sorteado:')))

lista = [n1, n2, n3]
sorteado = random.choice(lista)
print('O nome sorteado foi {}!!!'.format(sorteado).upper())