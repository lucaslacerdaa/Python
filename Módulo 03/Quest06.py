def maior(a: list):
    maior = 0
    for c in range(len(a)):
        if a[c] > maior:
            maior = a[c]

    print(f'O maior valor desse vetor é {maior}')

    v = []
    for c in range(5):
        x = int(input('Informe um valor:'))
        v.append(x)

    resultado = maior(v)

    print(resultado)