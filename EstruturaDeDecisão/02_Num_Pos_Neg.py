#Exibe na tela se o número é positivo ou negativo

nNumVal = int(input('Digite um número para validação: '))

if (nNumVal < 0):
    print('O número',nNumVal,'é negativo!')
elif (nNumVal > 0):
    print('O número',nNumVal,'é positivo!')
else:
    print('O número é igual a Zero!')
