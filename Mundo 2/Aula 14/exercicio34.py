sexo = 0

while sexo == 0:
    sexo = str(input("Digite o sexo de uma pessoa! [M/F]: "))
    if sexo == "M" or sexo == "F":
        print(f"Voce escolheu o sexo {sexo}!")
    else:
        print("Você não escolheu nenhuma opção correta, tente novamente! [M/F]")
        sexo = 0