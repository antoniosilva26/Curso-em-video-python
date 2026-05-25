peso = 0 
Maiorpeso = 0

for c in range(1, 6):
    peso = float(input("Digite seu peso: "))
    if(peso > Maiorpeso):
        Maiorpeso = peso
print(f"O maior peso é: {Maiorpeso}")