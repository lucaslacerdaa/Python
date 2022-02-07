v = []
maior = 0
menor = 1000000000000000000000000000000000

for c in range(10):
  x = int(input('Digite valores para alimentar esse vetor: '))
  v.append(x)

for c in range(10):
  if v[c] > maior:
    maior = v[c]

for c in range(10):
  if v[c] < menor:
    menor = v[c]


print()
print(f'O maior valor desse vetor é: {maior}.')
print(f'O menor valor desse vetor é: {menor}.')
