import math as matema

num = int(input("Digite um número"))

seno = matema.radians(num)
cosseno = matema.radians(num)
tang = matema.radians(num)



if matema.sin(cosseno) == 0:
    print(f"O Seno, Cosseno e Tangente de {matema.sin(seno)} é: {matema.sin(cosseno)}, {matema.sin(tang)}, Indefinido")
else:
    print(f"O Seno, Cosseno e Tangente de {num} é: {matema.sin(seno)} {matema.sin(cosseno)} {matema.sin(tang)}")