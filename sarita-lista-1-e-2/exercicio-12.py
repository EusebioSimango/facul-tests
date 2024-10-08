import os

os.system("cls")

nome = input("Digite um nome: ")
quantidade_a = nome.lower().count('a')

if quantidade_a == 0:
    print(f"O nome {nome} nao possui nenhuma letra 'a'.")
elif quantidade_a == 1:
    print(f"O nome {nome} possui uma letra 'a'.")
else:
    print(f"O nome {nome} possui {quantidade_a} letras 'a'.")
