import os

os.system("cls")

def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

for i in range(numero1, numero2 + 1):
    if eh_primo(i) == True:
        print(i)
