import math as matematica
import random as aleatorio

NomeAluno1 = str(input("Digite o nome do primeiro aluno"))
NomeAluno2 = str(input("Digite o nome do segundo aluno"))
NomeAluno3 = str(input("Digite o nome do terceiro aluno"))
NomeAluno4 = str(input("Digite o nome do quarto aluno"))

lista = [NomeAluno1, NomeAluno2, NomeAluno3, NomeAluno4]

print(lista)

result = aleatorio.sample(lista, 4)

print(f"A ordem será: {result}")