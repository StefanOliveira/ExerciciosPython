#Validação de Sexo

aSex = input('Digite M para "Masculino" e F para "Feminino": ').upper()

if (aSex == 'M'):
    print('Você é do sexo Masculino!')
elif (aSex == 'F'):
    print('Você é do sexo Feminino!')
else:
    print('Sexo inválido!')
