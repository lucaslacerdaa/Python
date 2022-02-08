import random

matriz = []
linha = 4
coluna = 4

for l in range(linha):
    lin = []
    for c in range(coluna):
        x = random.randint(1,99)
        lin.append(x)
    matriz.append(lin)

print('matriz')
for l in range(linha):
    for c in range(coluna):
        print(f'[{matriz[l][c]:02d}]', end='')
        print()

#somando os valores da matriz
soma = 0
for l in range(linha):
    for c in range(coluna):
        soma+=matriz[l][c]

print()
print(f'A soma de todos os valores da matriz é: {soma}')