n = int(input('\033[0mEscreva \033[0mum \033[0mnúmero \033[4;36;47mINTEIRO! \033[0m'))

c = str(input('Quer que eu converta para binário, hexadecimal ou octal?'))

c = c.upper()

if c in ['BINÁRIO', 'BINARIO']:
    b = bin(n)[2:]
    print('Seu número em código binário é {}.'.format(b))

elif c == 'OCTAL':
    o = oct(n)[2:]
    print('Seu número em octal é {}.'.format(o))

elif c in ['HEXADECIMAL', 'HEXA', 'HX']:
    h = hex(n)[2:]
    print('Seu número em hexadecimal é {}.'.format(h))

else:
    print('Não decidiu, robô desistiu, escreveu de gracinha, robô fechou sua panelinha!')