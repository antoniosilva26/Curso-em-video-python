"""Tuplas são imutáveis!!!, ou seja: vc n consegue mudar elas"""
lanche = ("Hamburger", "Suco", "Pizza", "Pudim")
print(lanche[2:3])

for c in lanche:
    print(c)

for cont in range(0, len[lanche]):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")
for comida in enumerate(lanche):
    print(f"Eu vou comer {comida}")

print(sorted(lanche))