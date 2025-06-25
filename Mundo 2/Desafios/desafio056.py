soma_idade = 0
homens = 0
mulheres_menores_20 = 0
idade_mulher_mais_velha = 0
for i in range(4):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()
    soma_idade += idade
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menores_20 += 1
    if sexo == 'F' and (idade > idade_mulher_mais_velha):
        idade_mulher_mais_velha = idade
media_idade = soma_idade / 4
print(f"Média de idade: {media_idade:.2f}")
print(f"Homens cadastrados: {homens}")
print(f"Mulheres com menos de 20 anos: {mulheres_menores_20}")
print(f"Idade da mulher mais velha: {idade_mulher_mais_velha}")
