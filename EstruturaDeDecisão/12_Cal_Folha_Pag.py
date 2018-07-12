#Cálculo Folha de pagamento

nValHor = float(input('Digite o valor da sua hora trabalhada: '))
nQtdHor = float(input('Digite a quantidade de horas trabalhadas: '))

nSalBrt = (nValHor * nQtdHor) #Cálculo para o salário bruto

#Salários até R$900,00 estão isentos de descontos
if (nSalBrt <= 900):
    print('Salário isento de descontos.')

#Salários até 1500
elif (nSalBrt > 900) and (nSalBrt <= 1500):
    print('Salário bruto      : R$',nSalBrt)

    #Descontos
    nIR = (nSalBrt * 0.05) #IR (Imposto de Renda)
    print('(-) IR(5%)         : R$',nIR)


elif (nSalBrt > 1500) and (nSalBrt <= 2500):
    print('Salário bruto      : R$',nSalBrt)

    #Descontos
    nIR = (nSalBrt * 0.10) #IR (Imposto de Renda)
    print('(-) IR(10%)        : R$',nIR)

elif (nSalBrt > 2500):
    print('Salário bruto      : R$',nSalBrt)

    #Descontos
    nIR = (nSalBrt * 0.20) #IR (Imposto de Renda)
    print('(-) IR(20%)        : R$',nIR)

#Valores Fixos

    nDscSin = (nSalBrt * 0.03) #Desconto Sindicato
    print('(-) Sindicato(3%)  : R$',nDscSin)
    
    nINSS = (nSalBrt * 0.10) #Desconto INSS
    print('(-) INSS(10%)      : R$',nINSS)

    nFGTS = (nSalBrt * 0.11) #Desconto FGTS - Empresa deposita, não influi no liquido
    print('FGTS (11%)         : R$',nFGTS)
    
    nTotDesc = (nIR + nDscSin + nINSS) #Total de Descontos
    print('Total de Descontos : R$',nTotDesc)

    #Salário liquido
    nSalLiq = (nSalBrt - nTotDesc)
    print('Salário liquido    : R$',nSalLiq)

else:
    print('Valor incorreto, verifique os dados digitados e tente novamente!')
    


