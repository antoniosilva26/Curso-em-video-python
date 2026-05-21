angulo1 = float(input("Digite o valor do primeiro ângulo: "))
angulo2 = float(input("Digite o valor do segundo ângulo: "))
angulo3 = float(input("Digite o valor do terceiro ângulo: "))

soma = angulo1 + angulo2 + angulo3

if angulo1 == 60 and angulo2 == 60 and angulo3 == 60:
    print("Com a soma dos triangulos, você pode formar um triângulo!")
else:
    print(f"Voce nao pode formar um triângulo, um triangulo tem 180 graus com lados iguais e seus angulos nao tem!\nSeu primeiro angulo tem: {angulo1}\nSeu segundo angulo tem: {angulo2}\nSeu terceiro angulo tem:{angulo3}")        