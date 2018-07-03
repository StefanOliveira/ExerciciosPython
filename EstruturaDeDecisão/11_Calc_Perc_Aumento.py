#Calcula o percentual de aumento conforme tabela salarial pré-definida

nSalCol = float(input("Digite o salário do colaborador: R$"))

#Salários até R$280,00
if nSalCol <= 280:
    nSalPer = 20 #Percentual de aumento

#Salários entre R$280,00 até R$700,00
elif nSalCol <= 700:
    nSalPer = 15 #Percentual de aumento

#Salários entre R$700,00 até R$1500,00
elif nSalCol <= 1500:
    nSalPer = 10 #Percentual de aumento

#Salários entre R$700,00 até R$1500,00
elif nSalCol > 1500:
    nSalPer = 5
            
nSalAum = nSalCol * (nSalPer / 100.0)
nNovSal = nSalCol + nSalAum

print('Salário antes do aumento: R$', nSalCol)
print('Percentual de aumento:', nSalPer,'%')
print('Valor do aumento: R$', nSalAum)
print("O novo salário do colaborador é: R$", nNovSal)
