#Validação de data digitada

print('\nDigite uma data para validação\n')

nDia = int(input('Digite o dia: '))
nMes = int(input('Digite o mês: '))
nAno = int(input('Digite o ano: '))

bVldData = False

#Valida meses com 31 dias
if(nMes == 1 or nMes == 3 or nMes == 5 or nMes == 7 or \
   nMes == 8 or nMes == 10 or nMes == 12):
    if(nDia <= 31):
        bVldData = True

#Valida meses com 30 dias
elif(nMes == 4 or nMes == 6 or nMes == 9 or nMes == 11):
    if(nDia <= 30):
        bVldData = True

#Valida mês de fevereiro se é ou bissexto
elif(nMes == 2):
    if(nAno % 4 == 0 and nAno % 400 != 0) or (nAno % 400 == 0):
        if(nDia <= 29):
            bVldData = True
    elif(nDia <= 28):
            bVldData = True

if(bVldData == True):
    print('Data',str(nDia)+'/'+str(nMes)+'/'+str(nAno),'válida')
else:
    print('Data digitada inválida, verifique os dados digitados')

            
    
