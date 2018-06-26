#Validação de Sexo

aNome = input('Digite seu nome: ')
aTurno = input('Em qual turno você estuda? Digite M para Matutino, V para Vespertino e N para Noturno: ').upper()

if(aTurno == 'M'):
    print('Bom dia,',aNome)
elif(aTurno == 'V'):
    print('Boa tarde,',aNome)
elif(aTurno == 'N'):
    print('Boa noite,',aNome)
else:
    print('Dados inválidos!')
      
