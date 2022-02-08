print('Questão 03')

escolha = int(input('informe um valor:'))

if escolha< 0:
    nome = input('Digite seu nome: ')
    nascimento = int(input('informe sue nascimento: '))
    ano_hj=int(input('Em que ano estamos: '))

    maior = ano_hj - nascimento
    if maior < 18:
        print(f'{nome}, não és maior de idade.')
    else:
        print(f'{nome}, és maior de idade.')

if escolha > 0:
    nome = input('Digite seu nome: ')
    profissão = input('informe sua profissão: ')
    salário = float(input('Qual seu salário: '))
    if salário < 901:
        print(f'{nome} , {profissão} - Cargo:   Supervisor')
    else:
        print(f'{nome} , {profissão} - Cargo:   Gerente')

if escolha == 0:
    nome = input('Digite seu nome: ')
    nome_animal = input('Digite o nome do seu pet: ')
    animal_idade = int(input(f'Digite o ano que {nome_animal} nasceu: '))

    ano= 2022
    print(f'{nome_animal} tem {ano - animal_idade} anos.')
