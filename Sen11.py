# EstruturaSequencial: peça 2 num intreio e 1 real, para cular

num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
num3 = float(input('Digite um número real: '))
a = (num1 * 2) + num2 / 2
b = num1 * 3 + num3
c = num3 ** 3
print(f'O produto do dobro do primeiro com metade do segundo é {a}\n'
      f'A soma do triplo do primeiro com metade do segundo {b}\n'
      f'O terceiro elevado ao cubo {c}')
