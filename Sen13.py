# EstruturaSequencial: peso ideal para homem e mulher

h = float(input('Digite sua altura: '))
man = 72.7 * h - 58
woman = 62.1 * h - 44.7
print(f'O peso ideal com altura de {h} para homem é {man:.2f}\n'
      f'O peso ideal com altura de {h} para mulher é {woman:.2f}')
