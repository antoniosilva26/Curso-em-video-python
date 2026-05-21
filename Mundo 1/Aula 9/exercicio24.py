nomecity = input("Digite o nome da sua cidade")

result = nomecity.find("Santo")

if result == 0:
    print(f"Sua cidade começa com Santo!")
else:
    print("Sua cidade nao começa com santo!")