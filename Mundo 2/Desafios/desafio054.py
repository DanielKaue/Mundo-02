maiores = 0
menores = 0
for i in range(7):
    idade = int(input(f"Idade da {i+1}ª pessoa: "))
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print(f"{maiores} maiores de idade e {menores} menores de idade.")
