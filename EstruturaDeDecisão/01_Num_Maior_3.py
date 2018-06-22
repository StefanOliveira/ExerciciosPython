#Imprime o maior número
nNum1 = int(input('Informe o primeiro número: '))
nNum2 = int(input('Informe o segundo número: '))
nNum3 = int(input('Informe o terceiro número: '))

if nNum1 == nNum2 and nNum1 == nNum3:
    print ('Os números são iguais!')
elif nNum1 > nNum2 and nNum1 > nNum3:
    print ('O maior número é:', num1)
elif nNum2 > nNum3:
    print ('O maior número é:', nNum2)
else:
    print ('O maior número é:', nNum3)
