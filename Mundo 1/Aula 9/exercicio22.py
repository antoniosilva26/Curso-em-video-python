nome = input("Digite seu nome completo")

letramai = nome.upper()
letramin = nome.lower()

contarsemesp = len(nome.replace(" ", ""))
primeironome = nome.split()

print(f"""
Seu nome com todas as letras maiúsculas é: {letramai}
Seu nome com todas as letras minúsculas é: {letramin}
Seu nome tem ao todo: {contarsemesp} letras!
Seu primeiro nome é: {primeironome[0]}

""")