chico = 1.50
ze = 1.10

ano = 0
while ze < chico:
  chico += 0.02
  ze += 0.03

  print()
  print(f'*Ano {ano+1}*')
  print(f'Chico. {chico:.2f} m.')
  print(f'Zé. {ze:.2f} m.')
  ano += 1


print()
print(f'Serão necessários {ano} anos para que Zé fique maior que Chico.')
