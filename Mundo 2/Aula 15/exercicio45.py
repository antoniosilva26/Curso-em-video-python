import random

vitorias = 0
num = 0
numeromaquina = 0
parouimpar = 0

while True:
    print("---------------------------------------------------------------------------")
    num = int(input("Jogo da velha contra a maquina, digite um número: "))
    print("---------------------------------------------------------------------------")
    parouimpar = str(input("Par ou Impar? [P/I]: "))
    numeromaquina = random.randrange(1, 10)
    if(parouimpar.strip().upper() != "P" and parouimpar.strip().upper() != "I"):
        print("Escolha uma opção válida [P/I]! Tente novamente!")
    elif((num + numeromaquina) % 2 == 0 and parouimpar.strip().upper() == "P"):
        print("---------------------------------------------------------------------------")
        print(f"Você jogou {num} e a máquina jogou {numeromaquina}, Total de {num + numeromaquina} deu PAR!")
        print("---------------------------------------------------------------------------")
        print("Você venceu!")
        vitorias = vitorias + 1
    elif((num + numeromaquina) % 2 == 0 and parouimpar.strip().upper() == "I"):
        print("---------------------------------------------------------------------------")
        print(f"Você jogou {num} e a máquina jogou {numeromaquina}, Total de {num + numeromaquina} deu PAR!")
        print("---------------------------------------------------------------------------")
        print("Você Perdeu!")
        print(f"Sequência de vitorias: {vitorias}")
        break
    elif((num + numeromaquina) % 2 >= 1 and parouimpar.strip().upper() == "P"):
        print("---------------------------------------------------------------------------")
        print(f"Você jogou {num} e a máquina jogou {numeromaquina}, Total de {num + numeromaquina} deu IMPAR!")
        print("---------------------------------------------------------------------------")
        print("Você Perdeu!")     
        print(f"Sequência de vitorias: {vitorias}")
        break  
    elif((num + numeromaquina) % 2 >= 1 and parouimpar.strip().upper() == "I"):
        print("---------------------------------------------------------------------------")
        print(f"Você jogou {num} e a máquina jogou {numeromaquina}, Total de {num + numeromaquina} deu IMPAR!")
        print("---------------------------------------------------------------------------")
        print("Você Ganhou!")  
        vitorias = vitorias + 1
    
