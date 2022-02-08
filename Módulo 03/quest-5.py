print('Questão 02')

valor = float(input('informe o valor do produto: '))

desconto = valor - valor*0.1
print(f'Valor com 10% de desconto: R${desconto:.2f}')

parcela = valor/3
print(f'Valor da parcela de 3x sem juros: R${parcela:.2f}')

comissão = desconto*0.05
print(f'Valor da comissão sendo a vista: R${comissão:.2f}')

comissão_prazo = valor*0.05
print(f'Valor da comissão sendo a prazo: R${comissão_prazo:.2f}')
