idade = int(input("Digite seu ano de nascimento!"))
contaidd = 2026 - idade

if contaidd == 18: 
    print("Ja está na hora de você se alistar!")
elif contaidd < 18:
    print(f"Ainda não está na hora de você de alistar! faltam {18-contaidd} anos!")
elif contaidd > 18:
    print(f"Você ja passou do prazo para se alistar, está {contaidd-18} anos fora do prazo!") 