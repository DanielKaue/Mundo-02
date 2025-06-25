for _ in range(1000): 
    entrada = input('Digite um número para ver a tabuada (ou "esc" para sair): ')
    
    if entrada.lower() == 'esc':
        print("Programa encerrado.")
        break

    if not entrada.isdigit():
        print("Digite um número válido.")
        continue

    n = int(entrada)
    print(f'{n} * 1 = {n*1}\n'
          f'{n} * 2 = {n*2}\n'
          f'{n} * 3 = {n*3}\n'
          f'{n} * 4 = {n*4}\n'
          f'{n} * 5 = {n*5}\n'
          f'{n} * 6 = {n*6}\n'
          f'{n} * 7 = {n*7}\n'
          f'{n} * 8 = {n*8}\n'
          f'{n} * 9 = {n*9}\n'
          f'{n} * 10 = {n*10}\n')

