alto = 0
posi_alto = 0
baixo = 10
posi_baixo = 0
v = []

for c in range(10):
  altura = float(input(f'Digite a altura do aluno {c+1}: '))
  v.append(altura)

for c in range(10):
  if v[c] > alto:
    alto = v[c]
    posi_alto = c
print(f'O maior aluno é o nº{posi_alto+1} com a estatura de {alto:.2f}m')

for c in range(10):
  if v[c] < baixo:
    baixo = v[c]
    posi_baixo = c
print(f'O menor aluno é o nº{posi_baixo+1} com a estatura de {baixo:.2f}m')

