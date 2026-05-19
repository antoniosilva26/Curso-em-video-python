import random

numero = random.randrange(1, 5)
print(numero)

pergunta = int(input("Digite um número entre 1 e 5 para tentar adivinhar qual número o computador escolherá!"))

if pergunta == numero:
    print(f"Você acertou! o número escolhido pelo computador foi {numero}, parabens!")
else:
    print(f"Você errou! o número escolhido pelo computador foi {numero}!")