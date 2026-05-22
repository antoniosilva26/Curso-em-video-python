lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))

if lado1 == lado2 and lado2 == lado3 and lado3 == lado1:
    print("Todos os lados sao iguais! É um triângulo Equilátero!")
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print("Tem dois lados iguais! É um triângulo Isósceles!")
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print("Todos os lados sao diferentes! É um triângulo Equilátero!")