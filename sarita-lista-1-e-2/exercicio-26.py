import os

os.system("cls")

def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

N = int(input("Digite um número N: "))
primos = []

for numero in range(2, N + 1):
    if eh_primo(numero) == True:
        primos.append(numero)

if len(primos) < 2:
    print("Não há primos suficientes.")
else:
    print(f"O segundo maior número primo é: {primos[-2]}")
