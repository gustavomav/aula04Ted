qtd_maca = int(input('Digite a quantidade de maçãs que você quer comprar '))

custo1 = qtd_maca * 1.30

custo2 = qtd_maca * 1.00

if qtd_maca < 12:
    print(f'O custo das maçãs será {custo1}')

else:
    print((f'O custo das maãs será {custo2}'))
