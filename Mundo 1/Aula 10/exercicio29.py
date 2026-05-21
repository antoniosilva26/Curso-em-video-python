velocidade = int(input("Digite a velocidade do veículo:"))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"Voce foi multado por excesso de velocidade! o limite é Km/h!, e você receberá uma multa de {multa}R$!")
else:
    print("Voce estava abaixo do excesso de velocidade! você não foi multadp")