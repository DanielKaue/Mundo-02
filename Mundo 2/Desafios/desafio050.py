soma = 0

for _ in range(6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma += n

print("A soma dos números pares é:", soma)
