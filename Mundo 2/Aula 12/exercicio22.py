import random

opcao = int(input("""Jokenpô! Escolha uma opção!
Pedra [1]
Papel [2]
Tesoura [3]
: """))

result = random.randint(1, 3)

if opcao == result:
    print("Empatou!")
    if result == 1:
        print("A maquina escolheu Pedra!")
    elif result == 2:
        print("A maquina escolheu Papel!")
    elif result == 3:
        print("A maquina escolheu Tesoura!")

elif opcao == 1 and result == 2 or opcao == 2 and result == 3 or opcao == 3 and result == 1:
    print("A maquina venceu!")
    if result == 1:
        print("A maquina escolheu Pedra!")
    elif result == 2:
        print("A maquina escolheu Papel!")
    elif result == 3:
        print("A maquina escolheu Tesoura!")

elif result == 1 and opcao == 2 or result == 2 and opcao == 3 or result == 3 and opcao == 1:
    print("Você venceu!")
    if result == 1:
        print("A maquina escolheu Pedra!")
    elif result == 2:
        print("A maquina escolheu Papel!")
    elif result == 3:
        print("A maquina escolheu Tesoura!")
