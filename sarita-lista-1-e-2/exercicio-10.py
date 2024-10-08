numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

contador = 0
for numero in range(numero1, numero2 - 1, -1):
    if numero % 2 != 0:
        print(numero)
        contador = contador + 1

if contador == 0:
    print(f"Não existe nenhum numero ímpar no intrvalo de {numero2} a {numero1}")
