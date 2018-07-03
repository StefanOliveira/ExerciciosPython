import math

nMesRec = input('Digite o mês recorrente: ')
nSalHora = float(input('Digite o seu salário por hora: '))
nHorTrab = float(input('Digite a quantidade de horas trabalhadas no período: '))

# Salário bruto no período
nSalBrt = nSalHora * nHorTrab

# Desconto INSS
nDscInss = (nSalBrt * 0.08)

# Desconto Sindicato
nDscSind = (nSalBrt * 0.05)

# Desconto IR
nDscIr = (nSalBrt * 0.11)

# Salário liquido
nSalLiq = (nSalBrt - nDscInss - nDscSind - nDscIr)

print ('\nAbaixo as informações referentes a',nMesRec)
print ('\nSalário Bruto {:.2f}'.format(nSalBrt))
print ('\nINSS {:.2f}'.format(nDscInss))
print ('\nSindicato {:.2f}'.format(nDscSind))
print ('\nImposto de Renda {:.2f}'.format(nDscIr))
print ('\nSalário Liquido {:.2f}'.format(nSalLiq))
