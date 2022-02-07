n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

if n1 == n2:
  print('Não é possivel somar números ímpares.')

else:
  if n2 < n1:
    maior = n1
    menor = n2

  if n1 < n2:
    maior = n2
    menor = n1

  resultado = 0

  while (menor <= maior):
    if(menor % 2 != 0):
      resultado += menor

    menor += 1

  print('O resultado é: ',resultado)
