
idade = 0
sexo = 0
c = 1
quer_cont = 0
count_idade = 0
count_cadastrados = 0
count_idade_fem = 0

while True:
    print("---------------------------------------------------------------------------")
    idade = int(input(f"Digite a idade da {c} pessoa!"))
    if idade > 18:
        count_idade = count_idade + 1
    print("---------------------------------------------------------------------------")
    sexo = str(input(f"Digite o sexo da {c} pessoa! [M/F]: "))
    if(sexo.strip().upper() != "M" and sexo.strip().upper() != "F"):
        print("Digite corretamente! [M/F]!")
    elif sexo.strip().upper() == "M":
        count_cadastrados = count_cadastrados + 1
    elif sexo.strip().upper() == "F" and idade < 20:
        count_idade_fem = count_idade_fem + 1
    print("---------------------------------------------------------------------------")
    quer_cont = str(input("Deseja continuar? [S/N]: "))
    if(quer_cont.strip().upper() == "N"):
        break
    c = c + 1
print("---------------------------------------------------------------------------")
print(f"Total de pessoas com mais de 18 anos: {count_idade}")
print(f"Ao todo temos {count_cadastrados} homens cadastrados!")
print(f"E temos {count_idade_fem} Mulhere(s) com menos de 20 anos!")