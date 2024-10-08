import os

os.system("cls")

divisiveis = []
N = int(input("Digite um número N: "))

for i in range(1, N + 1):
    if i % 5 == 0 and i % 3 == 0:
        divisiveis.append(i)

print(f"Números divisíveis por 5 e 3 entre 1 e {N}: {divisiveis}")
