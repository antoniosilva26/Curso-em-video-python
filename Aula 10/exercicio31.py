viagem = int(input("Qual a distância da viagem em km?"))

if(viagem <= 200):
    conta = 0.50 * viagem
    print(f"A viagem custará {conta}!")
else:
    conta = 0.45 * viagem
    print(f"A viagem custará {conta}!")    