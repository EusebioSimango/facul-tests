import os
numeros = []

os.system("cls")

for i in range(4):
    novo_numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(novo_numero)

print(f"Maior número: {max(numeros)}")
print(f"Menor número: {min(numeros)}")
