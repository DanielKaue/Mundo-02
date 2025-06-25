maior = menor = int(input("Digite um número: "))
for i in range(1, 5):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
