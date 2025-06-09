n1 = float(input('Qual a sua primeira nota? '))
n2 = float(input('E a segunda? '))
m = (n1 + n2) / 2

if m < 0 or m > 10:
    print('Nota de ET kkkkkkkkkkkkkkkkkkkkkkkk! Vai estudar, terráqueo! 👽')

elif m <= 4.9:
    print('Reprovado!')

elif 5 <= m <= 6:
    print('Você está de recuperação')

else:
    print('Você passou!')
