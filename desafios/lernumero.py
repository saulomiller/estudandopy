n = input("Digite um nuemro:")

if n.isdigit():
    print(f"Milhares: {n[-4] if len(n) > 3 else 0}")
    print(f"Centenas: {n[-3] if len(n) > 2 else 0}")
    print(f"Dezenas: {n[-2] if len(n) > 1 else 0}")
    print(f"Unidades: {n[-1]}")
else:
    print("Digite somente numeros")
