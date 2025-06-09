from datetime import datetime

ano_atual = datetime.now().year

d = int(input('Em que ano você nasceu? '))

i = ano_atual - d

if i < 0 or i > 100:
    print('Mó etezão KKKKKKKKKK')

elif i <= 9:
    print('Sua categoria é MIRIM!')

elif 10 <= i <= 14:
    print('Sua categoria é INFANTIL!')

elif 15 <= i <= 19:
    print('Sua categoria é JUNIOR!')

elif i == 20:
    print('Sua categoria é SÊNIOR!')

else:
    print('Sua categoria é MASTER!')
