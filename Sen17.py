# EstruturaSequencial: loja de tintas 2

area_pint = float(input('Digite a tamanho da área pintada em metros quadrados: '))
litros = area_pint / 6
latas = int(litros / 18)
galoes = litros / 3.6
mistura_lata = int(litros / 18)
mistura_galao = int(litros - (mistura_lata * 18) / 3.6)

print(f'A quantidade de latas a serem compradas é {latas} e valor total é R${latas * 80}\n '
      f'A quantidade de galões a serem comprados é {galoes} e o valor total é R${galoes * 25}\n'
      f'Mistura: ')
