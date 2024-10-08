import os

os.system("cls")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

contador = 0
for num in range(num2, num1 + 1):
    if num % 5 == 0:
        contador = contador + 1
        print(num)

if contador == 0:
    print(f"Nenhum numero no intervalo de {num2} a {num1} é divisivel por 5")
