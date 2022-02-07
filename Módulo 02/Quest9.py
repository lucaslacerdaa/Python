v = []
par = []
par_soma = 0
impar = []
impar_qtd = 0

for c in range(6):
    x = int(input('Digite números para alimentar o vetor: '))
    v.append(x)

for c in range(6):

    if v[c] % 2 == 0:
        par_soma += v[c]
        par.append(v[c])

    if v[c] % 2 == 1:
        impar_qtd += 1
        impar.append(v[c])

print('*' * 75)
print(f'Números Pares: {par}')
print(f'Números Impares: {impar}.')

print(f'Soma dos valores pares = {par_soma}')
print(f'Foram digitados {impar_qtd} números impares')




