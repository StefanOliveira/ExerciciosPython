#Valida se o ano é bissexto

import math

print('\n========Valida Ano Bissexto========\n')
nValAno = int(input('Digite o ano para validar: '))

bValBis = False

if(nValAno % 4 == 0):
    bValBis = True
    if(nValAno % 400 == 0) and (nValAno % 100 != 0):
        bValBis = False

if(bValBis):
    print('O ano informado é bissexto!')
else:
    print('Ano não é bissexto')
