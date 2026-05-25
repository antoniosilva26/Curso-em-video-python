import random

n = 0
palp = 0
quantpalp = 0
rando = 0

while n != 10:
    if rando == 0:
        rando = random.randrange(1, 10)
    n = n + 1
    palp = int(input("Tente adivinhar um número entre 1 e 10: "))
    if rando == palp:
        print("Você acertou o número! parabens!")
    else:
        quantpalp = quantpalp + 1
        print(f"Você errou! tente novamente! Quantidade de palpites: {quantpalp}")