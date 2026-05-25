num = int(input("Escolha um numero para fazer fatorial dele!"))
c = 0
soma = 0
num2 = num
while num2 >= 2:
    c = c + 1
    num2 = num2 - 1
    print(num * num2)
    num = num * num2
print(soma)