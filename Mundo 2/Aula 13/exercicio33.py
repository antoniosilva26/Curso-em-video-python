nome = 0
sexo = 0
homem = 0
mulher = 0
idade = 0
somaidade = 0
menorde20 = 0
maisvelho = 0
maisvelhoidd = 0
for c in range(1, 5):
    nome = str(input(f"Digite o nome da {c} pessoa:"))
    sexo = str(input(f"Digite o sexo da {c} pessoa: [M] ou [F]"))
    idade = int(input(f"Digite a idade da {c} pessoa:"))
    if sexo == "F" and idade < 20:
        menorde20 += 1
    if sexo == 'M' and idade > maisvelhoidd:
        maisvelhoidd = idade
        maisvelho = nome
    somaidade += idade

print(f"A media de idade do grupo é: {somaidade / 2}")
print(f"O nome do homem mais velho é: {maisvelho}")
print(f"A quantidade de mulheres com menos de 20 anos é: {menorde20}")