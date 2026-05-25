num = int(input("Digite um número"))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot+=1
    else:
        print('\033[31m', end='')
    print(c)
print(f"\033[m{num} pode ser divido {tot} vezes!")
if tot == 2:
    print("E por isso ele é um número primo!")
else:
    print("E por isso ele não é um numero primo!")