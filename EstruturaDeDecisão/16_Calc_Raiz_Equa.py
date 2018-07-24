#Calulo - Raizes de uma Equação de Segundo Grau

import math

print('Cálculo de equação de Segundo Grau: ax² + bx + c')
nVlrA = int( input('Coeficiente a: ') )
#Valida se é uma equação de segundo grau
if (nVlrA == 0):
    print('Se a = 0, O valor informado não forma uma Equação de Segundo Grau!')
nVlrB = int(input('Coeficiente b : '))
nVlrC = float(input('Coeficiente c : '))

# Calcula o Delta
nDlta = (nVlrB * nVlrB) - (4 * nVlrA * nVlrC)

if (nDlta < 0):
    print('Delta menor que 0, a equação não possui valores reais.')
elif (nDlta == 0):
    print('A equação possui apenas uma raiz')
    nRaiz = -nVlrB / (2 * nVlrA)
    print('Delta = 0, Raiz:', nRaiz)
else:
    print('A equação possui duas raizes')
    nRaiz1 = (-nVlrB + math.sqrt(nDlta)) / (2 * nVlrA)
    nRaiz2 = (-nVlrB - math.sqrt(nDlta)) / (2 * nVlrA)
    print('Raiz 1:', nRaiz1)
    print('Raiz 2:', nRaiz2)
