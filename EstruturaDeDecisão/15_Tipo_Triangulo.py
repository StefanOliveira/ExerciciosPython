#Informa qual é o tipo de Triangulo baseado nos dados informados

print('Insira os valores dos lados do Triangulo!')
nNum1 = float(input("Digite o primeiro lado: "))
nNum2 = float(input("Digite o segundo lado: "))
nNum3 = float(input("Digite o terceiro lado: "))

# Verifica se é um triangulo
if nNum1 > (nNum2 + nNum3) or nNum2 > (nNum1 + nNum3) or nNum3 > (nNum1 + nNum3):
    ValTriangulo = False
else:
    ValTriangulo = True

if ValTriangulo:
    print('Os valores inseridos formam um triangulo!')

    if nNum1 == nNum2 and nNum2 == nNum3:
        print('O triangulo é um "Equilátero"')

    elif nNum1 == nNum2 or nNum1 == nNum3 or nNum2 == nNum3:
        print('O triangulo é um "Isóceles"')

    else:
        print('O triangulo é um "Escaleno"')

else:
    print('Erro! Verifique os dados digitados, os valores inseridos não formam um triangulo')
