times = ("Palmeiras", "Flamengo", "Fluminense", "Athletico-PR", "Bragantino", "Coritiba", "São Paulo", "Bahia", "Cruzeiro", "Botafogo", "EC Vitória", "Atlético-MG", "Internacional", "Grêmio", "Corinthias", "Vasco da Gama", "Santos", "Mirassol", "Remo", "Chapecoense")
c = 0

for c in range(0, 5):
    print(f"Os 5 primeiros colocados são: {times[c]}")
print("-------------------------------------------------")
for c in range(15, 20):
    print(f"Os ultimos 5 colocados são: {times[c]}")
print("-------------------------------------------------")
print("A ordem alfabética dos times são:")
print(sorted(times))
print(f"A chapecoense está na colocação: {times.index("Chapecoense")}")