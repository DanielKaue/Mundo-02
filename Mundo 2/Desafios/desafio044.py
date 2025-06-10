p = float(input('Qual o preço do produto? R$ '))
f = input(
    'Escolha um método de pagamento:\n'
    '* Dinheiro ou cheque (à vista)\n'
    '* Cartão vista (5% desconto)\n'
    '* Cartão 2x (parcelado em 2x sem juros)\n'
    '* Cartão 3+ (parcelado em 3x ou mais com 20% de juros)\n'
    'Digite a opção: '
).strip().upper()

if f in ['DINHEIRO', 'CHEQUE']:
    valor_final = p
    print(f'Pagamento à vista em dinheiro/cheque. Valor final: R$ {valor_final:.2f}')

elif f == 'CARTÃO VISTA':
    valor_final = p * 0.95
    print(f'Pagamento à vista no cartão com 5% de desconto. Valor final: R$ {valor_final:.2f}')

elif f == 'CARTÃO 2X':
    valor_final = p
    parcela = valor_final / 2
    print(f'Parcelado em 2x sem juros. Cada parcela: R$ {parcela:.2f}. Total: R$ {valor_final:.2f}')

elif f == 'CARTÃO 3+':
    n = int(input('Quantas parcelas? (3 ou mais): '))
    if n < 3:
        print('Número inválido de parcelas para essa opção.')
    else:
        taxa_juros = 0.20
        valor_final = p + (p * taxa_juros)
        parcela = valor_final / n
        print(f'Parcelado em {n}x com 20% de juros. Cada parcela: R$ {parcela:.2f}. Total: R$ {valor_final:.2f}')

else:
    print('Opção inválida. Tente novamente.')
