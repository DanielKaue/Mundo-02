primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
for i in range(10):
    print(primeiro_termo + i * razao, end=" → ")
print("FIM!")
