altura = float(input("Digite sua altura"))
peso = float(input("Digite seu peso"))
print(altura*altura)
imc = peso / (altura * altura)


if imc < 18.5:
    print(f"Seu IMC é: {imc}"[:16])
    print("Você está abaixo do peso!")
elif imc >= 18.5 and imc < 25:
    print(f"Seu IMC é: {imc}"[:16])
    print("Você está no peso ideal!")
elif imc >= 25 and imc < 30:
    print(f"Seu IMC é: {imc}"[:16])
    print("Você está com sobrepeso!")
elif imc >= 30 and imc < 40:
    print(f"Seu IMC é: {imc}"[:16])
    print("Você está com obesidade!")
elif imc > 40:
    print(f"Seu IMC é: {imc}"[:16])
    print("Você está com obesidade mórbida!")