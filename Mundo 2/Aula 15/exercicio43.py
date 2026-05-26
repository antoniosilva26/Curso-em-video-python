n = 0
loop = 0
count = 0
soma = 0

while loop != 999:
    n = int(input("Digite um número [Digite 999 para parar]"))
    if n == 999:
        loop = 999
        break
    soma = soma + n
    count = count + 1
print(f"Você digiou {count} numeros e a soma de todos os resultados foi: {soma}")