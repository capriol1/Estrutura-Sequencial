# EstruturaSequencial: Rendimento diario de pesca

peso = float(input('Digite o valor dos peixes em quilos: '))
exesso = peso - 50
valor = exesso * 4
print(f'O peso total dos peixes em quilos é {peso}\n'
      f'O exesso em quilos é {exesso}\n'
      f'O valor por esse exesso é R${valor}')
