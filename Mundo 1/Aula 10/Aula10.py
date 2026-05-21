tempo = int(input("Quantos anos tem seu carro? "))


if tempo <= 3:
    print("Carro novo!")
else:
    print("Carro velho!")


nota1 = float(input("Digite a primeira nota"))
nota2 = float(input("Digite a segunda nota"))

media = (nota1 + nota2) / 2

if media >= 6.0:
    print(f"Nota: {media}, nota boa, parabens!")
else:   
    print("Nota ruim! estude mais")