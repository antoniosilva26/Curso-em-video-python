ano = int(input("Digite nosso ano atual: "))

if ano % 100 == 00:
    print("Seu ano é bissexto!")
else:
    if ano % 4 == 0:
        print("Seu ano é bissexto!")
    else:
        print("Seu ano não é bissexto!")


