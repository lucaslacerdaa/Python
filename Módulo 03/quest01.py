print('Questão 01')

lista = []

for c in range(4):
    n = float(input(f'Digite a {c + 1} nota: '))
    lista.append(n)

x = 0
for c in range(4):
    x += lista[c]

y = 0
for c in range(4):
    if lista[c] > y:
        y = lista[c]

z = 11
for c in range(4):
    if lista[c] < z:
        z = lista[c]

print('')
print(f'A menor nota:{z}')
print(f'A maior nota:{y}')
print(f'A média:{x / 4:.1f}')
