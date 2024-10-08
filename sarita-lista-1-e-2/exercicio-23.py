import os

os.system("cls")

numeros = []

for i in range(5):
    novo_numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(novo_numero)

numeros_sorteados = sorted(numeros)
print(f"Segundo maior número:: {numeros_sorteados[-2]}")
