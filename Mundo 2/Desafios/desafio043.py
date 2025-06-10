a = float(input('Digite sua altura em METROS: '))
p = float(input('Digite seu peso em KILOGRAMAS'))

imc = p/(a**2)

print(f'Seu IMC é: {imc:.2f}')

if imc < 0 or imc > 200:
    print('PESO DE ET KKKKKKKKKKK')
elif imc < 18.5:
    print('Classificação: Abaixo do peso')
elif imc < 25:
    print('Classificação: Peso normal')
elif imc < 30:
    print('Classificação: Sobrepeso')
elif imc < 35:
    print('Classificação: Obesidade grau 1')
elif imc < 40:
    print('Classificação: Obesidade grau 2')
else:
    print('Classificação: Obesidade grau 3 (mórbida)')