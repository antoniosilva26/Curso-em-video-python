import math as matematica
from random import *

NomeAluno1 = input("Digite o nome do primeiro aluno")
NomeAluno2 = input("Digite o nome do segundo aluno")
NomeAluno3 = input("Digite o nome do terceiro aluno")
NomeAluno4 = input("Digite o nome do quarto aluno")

result = randint(1, 4)

if result == 1:
    print(f"O aluno sorteado foi: {NomeAluno1}")
elif result == 2:
    print(f"O aluno sorteado foi: {NomeAluno2}")

elif result == 3:
    print(f"O aluno sorteado foi: {NomeAluno3}")
elif result == 4:
    print(f"O aluno sorteado foi: {NomeAluno4}")