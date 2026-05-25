s = 0
numimpar = 0
for c in range(1, 501, ):
    if c % 2 == 0 and c % 3 == 0:
        s += c
        numimpar += 1
print(f"A soma dos {numimpar} números pares são: {s}")
