num = 0
count = 0
loop = ""
soma = 0
while loop.upper() != "N":
    num = int(input("Digite um número: "))
    soma = soma + num
    count = count + 1
    loop = str(input("Quer continuar? [S/N]: "))
print(f"Voce digitou {count} numeros e a média deles foi: {soma / count}")