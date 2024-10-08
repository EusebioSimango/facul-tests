import os

os.system("cls")

nome = input("Digite seu nome completo: ")
iniciais = [parte[0].upper() for parte in nome.split()]
print(".".join(iniciais) + ".")
