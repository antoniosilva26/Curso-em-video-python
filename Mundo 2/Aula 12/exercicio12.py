valorcasa = int(input("Qual será o valor da casa?"))
salario = int(input("Digite o salário do comprador"))
anospag = int(input("Em quantos anos você irá pagar?"))
porcentagemsalario =  salario * 0.30
prestacao = valorcasa / (anospag * 12)

if prestacao > porcentagemsalario:
    print("Prestacao negada!")

else: 
    print("Parabens! seu pedido de empréstimo foi aceito!")
