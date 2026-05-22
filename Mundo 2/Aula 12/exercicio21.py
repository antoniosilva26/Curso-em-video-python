valor = int(input("Digite o valor a ser pago: "))
escolha = int(input("""De qual forma você deseja realizar o pagamento?
A vista no dinheiro/cheque(10 porcento de desconto) [1]
A vista no cartão(5 porcento de desconto) [2]
Em até 2x no cartão(preço normal) [3]
3x ou mais no cartão(20 porcento de juros) [4]: """))

if escolha == 1:
    desconto = valor - (valor * 0.10)
    print(f"Você recebeu 10 porcento de desconto por pagar a vista no dinheiro/cheque! Agora você pagará só {desconto}! {valor * 0.10} a menos!")
if escolha == 2:
    desconto = valor - (valor * 0.05)
    print(f"Você recebeu 5 porcento de desconto por pagar a vista no cartão! Agora você pagará só {desconto}! {valor * 0.05} a menos!")
if escolha == 3:
    print(f"Você não recebeu nenhum desconto por pagar no cartao em 2x! Você pagará o valor normal({valor})!")
if escolha == 4:
    juros = valor + ((valor * 0.20))
    print(f"Você escolheu pagar em 3x ou mais no cartão e irá pagar 20% de juros! Você irá pagar no total {juros}!")
