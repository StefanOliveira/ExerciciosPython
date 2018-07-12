#Exibe dia da semana referente ao número digitado

dia_sem = ('Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo')
nDiaSem = (input('Digite o número para saber o dia da Semana: '))

if nDiaSem < '0' or nDiaSem > '6':
    print('Erro, digite valores entre 0 e 6')

else:
    aNind = int(nDiaSem[0:1])-1
    Dia_Sem = (dia_sem[aNind])
    print('O número digitado é referente a:',Dia_Sem)

