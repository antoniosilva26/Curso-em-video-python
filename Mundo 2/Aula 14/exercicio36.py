num = 1
numescol1 = 0
numescol2 = 0
while num != 0:
    numescol1 = int(input("Digite um número: "))
    numescol2 = int(input("Digite outro número: "))
    escol = int(input("""Digite a opção que você deseja realizar:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa"""))
    if escol == 1:
        print(f"O resultado desta operação foi: {numescol1+numescol2}")
        num = 0
    elif escol == 2:
        print(f"O resultado desta operação foi: {numescol1*numescol2}")
        num = 0
    elif escol == 3:
        if numescol1 > numescol2:
            print(f"O resultado desta operação foi: {numescol1} é maior que {numescol2}!")
        else:
            print(f"O resultado desta operação foi: {numescol2} é maior que {numescol1}!")
        num = 0
    elif escol == 5:
        num = 0
    else:
        continue
