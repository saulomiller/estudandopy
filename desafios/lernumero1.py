n = int(input(f"Digite um Numero:"))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print(f"Analisando  o numero: {n}")
print(f"Unidade:{u}")
print(f"Dezena:{d}")
print(f"Centena:{c}")
print(f"Milhar:{m}")
