import random
import time
import os

def jogar_novamente_ou_menu():
    while True:
        print("\nQueres jogar de novo ou voltar ao menu principal?")
        print("1. Jogar novamente")
        print("2. Voltar ao menu principal")
        
        opcao = input("\nEscolha uma opção (1 ou 2): ")
        
        if opcao == "1":
            return True
        elif opcao == "2":
            return False
        else:
            print("\nOpção inválida. Tente novamente.")

def jogar_quebra_cabeca_com_espelhos():
    while True:
        tentativas = 0
        max_tentativas = 3
        
        os.system('cls')
        print("\nEstás numa sala com espelhos por todos os lados e apenas uma porta verdadeira.")
        print("A porta pode estar em qualquer direção: Esquerda, Direita, Trás ou Frente.")
        print("Tens 3 tentativas para escapar antes que um gás radioativo seja liberado.\n")

        while tentativas < max_tentativas:
            porta_certa = random.randint(1, 4)
            
            print("Escolhe uma direção:")
            print("1. Esquerda")
            print("2. Direita")
            print("3. Trás")
            print("4. Frente")
            
            escolha = int(input("\nDigite o número da sua escolha (1 a 4): "))
            
            if escolha == porta_certa:
                os.system('cls')
                print("\nParabéns! Encontraste a porta certa e escapaste com vida!")
                break
            else:
                tentativas += 1
                print(f"\nPorta errada! Tentativas restantes: {max_tentativas - tentativas}")
                
            time.sleep(1)
        
        if tentativas == max_tentativas:
            os.system('cls')
            print("\nInfelizmente, todas as tentativas falharam!")
            print("Um gás radioativo foi liberado na sala... morreste.")
        
        if not jogar_novamente_ou_menu():
            return

def jogar_casa_assombrada():
    while True:
        tentativas = 0
        max_tentativas = 2
        
        os.system('cls')
        print("\nEstás numa casa assombrada! Há fantasmas por todo o lado, tentando sugar a tua alma.")
        print("Tens várias opções para escapar: Porta dos Fundos, Porta Principal, Janela ou Telhado.")
        print("Apenas uma dessas saídas é segura. Tens 2 tentativas para escapar antes que os fantasmas te apanhem!\n")
        
        while tentativas < max_tentativas:
            saida_certa = random.randint(1, 4)
            
            print("Escolhe uma saída:")
            print("1. Porta dos Fundos")
            print("2. Porta Principal")
            print("3. Janela")
            print("4. Telhado")
            
            escolha = int(input("\nDigite o número da sua escolha (1 a 4): "))
            
            if escolha == saida_certa:
                os.system('cls')
                print("\nParabéns! Conseguiste escapar dos fantasmas!")
                break
            else:
                tentativas += 1
                print(f"\nSaída errada! Tentativas restantes: {max_tentativas - tentativas}")
                
            time.sleep(1)
        
        if tentativas == max_tentativas:
            os.system('cls')
            print("\nInfelizmente, todas as tentativas falharam!")
            print("Os fantasmas sugaram a tua alma... morreste.")
        
        if not jogar_novamente_ou_menu():
            return


while True:
    os.system('cls')
    print("\n*** Menu Principal ***")
    print("1. Jogar Espelho")
    print("2. Jogar Casa Assombrada")
    print("3. Sair")
	
    opcao = input("\nEscolha uma opção (1, 2 ou 3): ")
	
    if opcao == "1":
        jogar_quebra_cabeca_com_espelhos()
    elif opcao == "2":
        jogar_casa_assombrada()
    elif opcao == "3":
        print("\nSaindo do jogo... Adeus!")
        break
    else:
        print("\nOpção inválida. Tente novamente.")

