s = 0
nasc = 0

for c in range(1, 8):
    nasc = int(input(f"Digite a {c} data de nascimento: "))
    if((2026 - nasc) >= 18):
        s += 1
print(f"{s} Pessoas ja atingiram a maioridade!")
