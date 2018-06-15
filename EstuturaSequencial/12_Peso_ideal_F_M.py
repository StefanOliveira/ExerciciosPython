import math

aSex = input('Digite o seu sexo, M para masculino e F para feminino: ').lower()
nAlt = float(input('Digite a sua altura: '))

if aSex == 'm':
    nPes = print('O seu peso ideial é: {:.2f}'.format((72.7 * nAlt) - 58))
elif aSex == 'f':
    nPes = print('O seu peso ideial é: {:.2f}'.format((62.1 * nAlt) - 44.7))
    
