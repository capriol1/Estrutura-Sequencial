# EstruturaSequencial: calcule e informe o tempo aproximado de download

mb = float(input('Digite o tamanho do arquivo para download em MB: '))
mbps = float(input('Digite a velocidadae de um link de Internet em Mbps: '))
tempo = mb / mbps
print(f'O tempo aproximado de download do arquivo usando este link {mbps} é de {tempo:.2f} minutos ')
