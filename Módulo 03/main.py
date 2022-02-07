i = 1
maior = 0
menor = 11


alunos = int(input("Quantidade de Alunos: "))

while i <= alunos:

   nota = int(input("Nota: "))

   if nota > maior:
       maior = nota

   if nota < menor:
       menor = nota

   i = i + 1

print("Maior Nota: %d" % (maior))
print("Menor Nota: %d" % (menor))