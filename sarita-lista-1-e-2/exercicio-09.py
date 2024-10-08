import os

os.system("cls")

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

contador = 0
for numero in range(numero1 + 1, numero2):
    if numero % 2 == 0:
        contador = contador + 1
        print(numero)

if contador == 0:
    print(f"Não existe nenhum número par entre {numero1} e {numero2}")
