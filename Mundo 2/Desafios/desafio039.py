from datetime import datetime

ano_atual = datetime.now().year

n = int(input('Em que ano você nasceu? '))

i = ano_atual - n

if i < 0 or i > 100:
    print('Mano é um ET kkkkkkkkkkk')
elif i < 18:
    print('Você ainda terá que se alistar ao exército! (Se você for do gênero masculino!)')
elif i == 18:
    print('Esse ano você terá que se alistar ao exército! (Se você for do gênero masculino!)')
else:
    print('Você não precisa mais se alistar ao exército!')
