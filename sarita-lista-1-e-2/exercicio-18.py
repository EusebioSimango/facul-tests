import os

os.system("cls")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = sum(range(min(num1, num2), max(num1, num2) + 1))
print(f"Soma de todos os números: {soma}")

impares = [num for num in range(min(num1 + 1, num2 + 1), max(num1, num2)) if num % 2 != 0]
print(f"Os 3 primeiros ímpares: {impares[:3]}")

pares = [num for num in range(min(num1 + 1, num2 + 1), max(num1, num2)) if num % 2 == 0]
print(f"Os 2 últimos pares: {pares[-2:]}")
