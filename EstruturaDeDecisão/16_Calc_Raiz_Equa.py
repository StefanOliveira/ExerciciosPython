#Calulo - Raizes de uma Equação de Segundo Grau

import math

print('Cálculo de equação de Segundo Grau')
nVlrA = float(input('Informe o valor de a : '))
nVlrB = float(input('Informe o valor de b : '))
nVlrC = float(input('Informe o valor de c : '))

#Valida se é uma equação de segundo grau
if (nVlrA == 0):
    print('Os valores informados não formam uma Equação de Segundo Grau!')
else:
    # Calcula o Delta
    nDlta = math.pow(nVlrB, 2) - (4 * nVlrA * nVlrC)

    if (nDlta < 0):
        print('A equação não possui valores reais.')
    elif (nDlta == 0):
        print('A equação possui apenas uma raiz')
        nRaiz = -(nVlrB) / (2 * valorA)
        print('Raiz:', nRaiz)
    else:
        print('A equação possui duas raizes')
        nRaiz1 = (-(valorB) + math.sqrt(nDlta)) / (2 * nVlrA)
        nRaiz2 = (-(valorB) - math.sqrt(nDlta)) / (2 * nVlrA)
        print('Raiz 1:', nRaiz1)
        print('Raiz 2:', nRaiz2)
