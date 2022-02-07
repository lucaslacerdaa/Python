v = []

for c in range(5):
    x = int(input('Informe um valor para alimentar o vetor: '))
    v.append(x)

while True:
    codigo = int(input('Informe um código de ação: '))
    print()
    if codigo == 1:
        print('Vetor na ordem direta de escrita')
        print(v)
        print()

    elif codigo == 2:
        c = 4
        v2 = []
        print('Vetor na ordem inversa de escrita')
        while c >= 0:
            v2.append(v[c])
            c -= 1
        print(v2)
        print()

    elif codigo == 0:
        print('FINALIZANDO O PROGRAMA!!')
        break

    else:
        print('Digite uma opção válida!')
