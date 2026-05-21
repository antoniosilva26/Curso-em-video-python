num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
num3 = int(input("Digite o terceiro número:"))

lista = [num1, num2, num3]
lista.sort()

print(f"O maior número da lista é: {lista[2]}, e o menor é: {lista[0]}")
