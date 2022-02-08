idade = 0
contador = 0
media = 0
maior = -1
menor = 125
maioridade = 0

lista = []
while True:
    valor = int(input('Informe idade: '))

    if valor > 0:
        idade += valor
        contador += 1
        lista.append(valor)
    else:
        break

    for c in range(len(lista)):
        if lista [c] > maior:
            maior = lista[c]
    for c in range(len(lista)):
        if lista [c] < menor:
            menor = lista[c]
    for c in range(len(lista)):
        if lista [c] > 18:
            maioridade += 1

media = idade/contador
print(f'Média das idades: {media} anos.')
print(f'Maior idade: {maior} anos.')
print(f'Menor idade: {menor} anos.')
print(f'No grupo tem: {maioridadei} pessoa(s) com mais de 18 anos.')