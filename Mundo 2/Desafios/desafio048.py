soma = 0

for num in range(1, 501, 2):  
    if num % 3 == 0:
        soma += num

print("A soma dos números ímpares múltiplos de 3 entre 1 e 500 é:", soma)
