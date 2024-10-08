import os

os.system("cls")

numeros = []
N = int(input("Quantos números serão digitados? "))

for i in range(N):
    novo_numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(novo_numero)

print(f"Maior número: {max(numeros)}")
print(f"Menor número: {min(numeros)}")
