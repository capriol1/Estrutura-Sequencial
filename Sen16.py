# EstruturaSequencial: Lojoa de tintas

area_pint = float(input('Digite a tamanho da área pintada em metros quadrados: '))
litros = area_pint / 3
latas = int(litros / 18)
print(f'A quantidade de latas a serem compradas é {latas} e valor total é R${latas * 80}')
