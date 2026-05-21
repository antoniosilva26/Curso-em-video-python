nasc = int(input("Digite seu ano de nascimento"))
idade = 2026 - nasc

if idade <= 9:
    print(f"Idade:{idade}\nEstá na categoria Mirim.")
elif idade > 9 and idade <= 14:
    print(f"Idade:{idade}\nEstá na categoria Infantil.")
elif idade > 14 and idade <= 19:
    print(f"Idade:{idade}\nEstá na categoria Junior.")
elif idade > 19 and idade <= 20:
    print(f"Idade:{idade}\nEstá na categoria Sênior.")
elif idade > 20:
    print(f"Idade:{idade}\nEstá na categoria Master.")