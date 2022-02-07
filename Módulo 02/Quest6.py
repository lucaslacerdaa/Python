v = []
positivo = 0
negativo = 0
for c in range(10):
    x = int(input('Informe um número para alimentar o vetor: '))
    v.append(x)

for c in range(10):
    if v[c] > 0:
        positivo += v[c]

    if v[c] < 0:
        negativo += 1

print()
print(f'Soma dos números positivos = {positivo}')
print(f'{negativo} número(s) negativo(s)')

