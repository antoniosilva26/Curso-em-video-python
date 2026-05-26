num = 0
c = 1
while True:
    num = int(input("Quer ver a tabuada de qual valor?"))
    if num  < 0: 
        break
    while c < 11:
        print(f"{num} x {c} = {num * c}")
        c = c + 1
    c = 1