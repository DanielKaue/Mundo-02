import random

print('Vamos jogar Jokenpô! Escolha entre: Pedra, papel e tesoura!')

j = str(input('Faça sua escolha: ')).strip().upper()
c = ['PEDRA','PAPEL','TESOURA']

vc = random.choice(c)

if j == vc:
    print('Empate...😒')

elif j == 'PEDRA' and vc == 'TESOURA' or j == 'PAPEL' and vc == 'PEDRA' or j == 'TESOURA' and vc == 'PAPEL':
    print('Você ganhou, mas roubando até eu né! 😡')

elif vc == 'PEDRA' and j == 'TESOURA' or vc == 'PAPEL' and j == 'PEDRA' or vc == 'TESOURA' and j == 'PAPEL':
    print('Achei fácil demais KKKKKKKKK🤫🤣🤣🤣🤣')

else:
    print('Isso é uma competição séria de jokenpô, ou somos crianças para ficar brincando de escrever coisas aleatórias?')