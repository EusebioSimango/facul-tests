import random
import os

os.system("cls")

N = 9
tentativa = 1

while N > 1:
    sorteado = random.randint(1, N)
    chute = int(input(f"Tentativa {tentativa}: Tente adivinhar um número entre 1 e {N}: "))

    os.system("cls")  # No Windows, em outros sistemas pode ser "clear"

    if chute == sorteado:
        print(f"Parabéns! Você acertou o número {sorteado}.")
        break
    else:
        print(f"Tentativa {tentativa}: Você digitou {chute} e o número sorteado foi {sorteado}.")
        N -= 1
        tentativa += 1

if N == 1:
    print("Você perdeu o jogo.")
