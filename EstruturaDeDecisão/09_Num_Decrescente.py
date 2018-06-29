#Imprime números em ordem decrescente

nNum1 = int(input('Digite o primeiro número: '))
nNum2 = int(input('Digite o segundo número: '))
nNum3 = int(input('Digite o terceiro número: '))

if nNum1 >= nNum2 and nNum1 >= nNum3:
    print(nNum1)
    if (nNum2 >= nNum3):
        print (nNum2)
        print (nNum3)
    else:
        print (nNum3)
        print (nNum2)
elif nNum2 >= nNum3:
    print (nNum2)
    if (nNum1 >= nNum3):
        print (nNum1)
        print (nNum3)
    else:
        print (nNum3)
        print (nNum1)
else:
    print (nNum3)
    if nNum1 >= nNum2:
        print (nNum1)
        print (nNum2)
    else:
        print (nNum2)
        print (nNum1)
