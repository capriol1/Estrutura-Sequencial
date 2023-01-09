# EstruturaSequencial: calcule e mostre o total do salário

gan = float(input('Digite quanto ganha por hora: '))
hora = int(input('Digite quantas hora trabalhadas por mês: '))
sal_bruto = gan * hora
ir = sal_bruto * 0.11
inss = sal_bruto * 0.08
sin = sal_bruto * 0.05
sal_liq = sal_bruto - ir - inss - sin
print(f'O salário bruto é {sal_bruto}\n'
      f'O desconto do Imposto de Renda é R${ir}\n'
      f'O desconto do INSS é R${inss}\n'
      f'O desconto do sindicato é R${sin}\n'
      f'O salário líquido é R${sal_liq}')
