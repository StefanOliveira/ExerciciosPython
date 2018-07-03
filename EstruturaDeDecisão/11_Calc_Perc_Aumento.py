#Calcula o percentual de aumento conforme tabela salarial pré-definida

nSalCol = float(input("Digite o salário do colaborador: R$"))
nSalAum = nSalCol

if nSalCol < 0:
    raise ValueError('Número negativo!')

    #Salários até R$280,00
    if nSalCol <= 280:
        print('Salário antes do aumento: R$',nSalCol)
        print('Percentual de aumento: R$',(nSalCol * 0.20))
        nSalAum += (nSalCol * 0.20)
        print("O novo salário do colaborador é: R$",nSalAum)

    #Salários entre R$280,00 até R$700,00
    elif nSalCol > 280 and nSalCol <= 700:
        print('Salário antes do aumento: R$',nSalCol)
        print('Percentual de aumento: R$',(nSalCol * 0.15))
        nSalAum += (nSalCol * 0.15)
        print("O novo salário do colaborador é: R$",nSalAum)

    #Salários entre R$700,00 até R$1500,00
    elif nSalCol > 700 and nSalCol <= 1500:
        print('Salário antes do aumento: R$',nSalCol)
        print('Percentual de aumento: R$',(nSalCol * 0.10))
        nSalAum += (nSalCol * 0.10)
        print("O novo salário do colaborador é: R$",nSalAum)

    #Salários entre R$700,00 até R$1500,00
    elif nSalCol > 1500:
        print('Salário antes do aumento: R$',nSalCol)
        print('Percentual de aumento: R$',(nSalCol * 0.05))
        nSalAum += (nSalCol * 0.05)
        print("O novo salário do colaborador é: R$",nSalAum)

