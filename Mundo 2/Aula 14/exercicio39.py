primtermo = int(input("Digite o primeiro termo!"))
raz = int(input("Digite a razao!"))

c = primtermo
e = 1
resp = 0

while e != 0:
    print(c)
    c = c + raz
    e = e + 1
    if e == 10 or e == resp:
        resp = int(input("Quantos termos você desenha mostrar a mais? Digite 0 caso nao queira mais nenhum"))
        if resp == 0:
            e = 0
        else:
            e = e - resp 