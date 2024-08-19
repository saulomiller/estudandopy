n = str(input("Digite seu nome:")).strip()
n = n.upper()
n_sem_espacos = n.replace(" ", "")
print(n,"\nSeu nome possui", len(n_sem_espacos), "letras")
