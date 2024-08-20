frase = str(input("Digite uma Frtase: ")).strip().upper()
print (f"A letra A aparecesa {frase.count("A")} vez na frase")
print (f"A primeira letra A apareceu na posicao {frase.find("A")+1}")
print (f"A Ultima letra A apareceu na posicao {frase.rfind("A")+1}")