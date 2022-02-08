chave = 3
mensagem = input('informe a mensagem para ser criptografada: ')

nA = ord('A')
nZ = ord('Z')
na = ord('a')
nz = ord('z')

cifrada = ''

for c in mensagem:
    ind = ord(c)
    if nA <= ind <= nZ:
        nova_letra = chr((ind+chave)%(nZ+1)+ ((ind+chave)//(nZ+1))*nA)
        cifrada = cifrada + nova_letra
    elif ind in range(na, nz + 1):
        nova_letra = chr((ind+chave)%(nz+1)+((ind+chave)//(nZ+1))*nA)
        cifrada = cifrada + nova_letra
    else: cifrada + c

print()
print(f'Mensagem criptografada: {cifrada}')
