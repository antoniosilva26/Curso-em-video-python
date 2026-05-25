numimpar = 0
soma = 0
for c in range(1, 7):
    print(c)
    if(c %2 == 0):
        soma += c
        numimpar += 1
print(f"A soma de {numimpar} números pares são: {soma}")
