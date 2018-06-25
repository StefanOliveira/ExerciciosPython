#Verifica qual dos 3 números é o menor
nNum1 = int(input('Digite o primeiro número: '))
nNum2 = int(input('Digite o primeiro número: '))
nNum3 = int(input('Digite o primeiro número: '))

#Validando o menor número
if(nNum1 == nNum2) and (nNum1 == nNum3):
    print('Os números são iguais!')
elif(nNum1 < nNum2) and (nNum1 < nNum3):
    print('O menor número é o:',nNum1)
elif(nNum2 < nNum3):
    print('O menor número é o:',nNum2)
else:
    print('O menor número é o:',nNum3)

#Validando o maior número
if(nNum1 == nNum2) and (nNum1 == nNum3):
    print('Os números são iguais!')
elif(nNum1 > nNum2) and (nNum1 > nNum3):
    print('e o maior número é o:',nNum1)
elif(nNum2 > nNum3):
    print('e o maior número é o:',nNum2)
else:
    print('e o maior número é o:',nNum3)


