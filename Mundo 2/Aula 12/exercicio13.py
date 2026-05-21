num = int(input("Escolha um número: "))

escolha = int(input("Escolha a base de conversão: \nBinario [1]\nOctal [2]\nHexadecimal [3]\n:"))

if escolha == 1:
    print(f"A conversao para número Binário foi: {bin(num)[2:]}")
if escolha == 2:
    print(f"A conversao para número Octal foi: {oct(num)[2:]}")
if escolha == 3:
    print(f"A conversao para número Hexadecimal foi: {hex(num)[2:]}")