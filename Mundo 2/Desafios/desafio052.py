numero = int(input("Digite um número: "))
if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            print(f"{numero} não é primo.")
            break
    else:
        print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")
