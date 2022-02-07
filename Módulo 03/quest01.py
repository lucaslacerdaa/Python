nota01 = int(input("Nota 1: "))
nota02 = int(input("Nota 2: "))
nota03 = int(input("Nota 3: "))
nota04 = int(input("Nota 4: "))

media = (nota01+nota02+nota03+nota04)/3

maior = 0
menor = 11



while i <= 4:

   if nota > maior:
       maior = nota

   if nota < menor:
       menor = nota

   i = i + 1

print("Media do aluno: %d" % (media))
print("Maior Nota: %d" % (maior))
print("Menorr Nota: %d" % (menor))



