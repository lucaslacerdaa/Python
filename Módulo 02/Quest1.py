print("Insira os dados")
n1 = float(input("Digite valor da hora: "))
n2 = float(input("Digite número de horas trabalhadas no mês:  "))

salario = (n1 * n2)
salarioLiq = salario - ((salario/100)*8)

if (salarioLiq >= 1000.00 and salarioLiq <= 1999.00):
    print("Salário do vendedor é de: R$", salarioLiq)
    pass
if (salarioLiq >= 2000.00 and salarioLiq <= 2999.00):
    print("Salário do gerente de vendas é de: R$", salarioLiq)
    pass
if (salarioLiq >= 3000.00 and salarioLiq <= 3999.00):
    print("Salário do gerente de loja é de: R$", salarioLiq)
    pass
if (salarioLiq >= 4000.00):
    print("Salário do presidente é de: R$", salarioLiq)
    pass
else: print("Valor inválido.")