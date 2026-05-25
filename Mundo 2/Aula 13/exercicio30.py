palavra = str(input("Digite uma palavra!"))
quantpala = len(palavra.replace(" ", ""))
print(quantpala)


for c in range(quantpala, 0, -1):
    print(palavra.find(quantpala))