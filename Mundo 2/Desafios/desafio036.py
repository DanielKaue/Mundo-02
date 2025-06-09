c = float(input('Qual o valor da casa? '))
s = float(input('Qual o seu salário? '))
p = float(input('Em quantos anos vai pagar? '))

prestacao_mensal = c / (p * 12)
limite = s * 0.30

if prestacao_mensal < limite:
    print('Você pode pagar a casa! Sairá por R${:.2f} por mês!'.format(prestacao_mensal))
elif prestacao_mensal == limite:
    print('Você até pode pagar pela casa, mas não sobrará nada. Sairá por R${:.2f} por mês, atingindo os 30%!'.format(prestacao_mensal))
else:
    print('Você não poderá pagar a casa, pois a parcela mensal ultrapassa 30% do seu salário.')
