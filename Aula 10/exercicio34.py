salario = int(input("Digite o salário do seu funcionário: "))


if salario >= 1250:
    conta = salario * 0.10
    print(f"O seu funcinario a partir de agora receberá o novo salário de {conta+salario}!")
else:
    conta = salario * 0.15
    print(f"O seu funcinario a partir de agora receberá o novo salário de {conta+salario}!")    