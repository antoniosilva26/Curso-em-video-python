nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media < 5.0:
    print(f"Você tirou {media} e ficou reprovado!!")
elif media >= 5.0 and media <= 6.9:
    print(f"Você tirou {media} e ficou de recuperação!")
elif media >= 7.0:
    print(f"Parabens! você tirou a nota {media} e foi aprovado!")