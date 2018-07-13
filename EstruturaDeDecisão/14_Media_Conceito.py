#Valida média e converte média para conceitos entre A à E

#Validação da nota 1
valid_nota = False
while valid_nota == False:
    nota1 = input('Digite a nota da primeira prova: ')
    try:
        nota1 = float(nota1)
        if nota1 < 0 or nota1 > 10:
            print('Nota inválida, valor deve ser entre 0 e 10')
        else:
            valid_nota = True
    except:
        print("Nota inválida, use apenas números separados por'.'(Ex: 9.5)")

#Validação da nota 2
valid_nota = False
while valid_nota == False:
    nota2 = input('Digite a nota da segunda prova: ')
    try:
        nota2 = float(nota1)
        if nota2 < 0 or nota2 > 10:
            print('Nota inválida, valor deve ser entre 0 e 10')
        else:
            valid_nota = True
    except:
        print("Nota inválida, use apenas números separados por'.'(Ex: 9.5)")
print('Nota 1: ',nota1)
print('Nota 2: ',nota2)

#Calcula média
media = (nota1+nota2)/2
print('Media: ',media)

#Valida média e informa se o aluno foi aprovado ou reprovado baseado no conceito
if media >= 9.0 and media <= 10.0:
    conceito = 'A'
    print('Aluno passou com nota: ',conceito)
elif media >= 7.5 and media < 9.0:
    conceito = 'B'
    print('Aluno passou com nota: ',conceito)
elif media >= 6.0 and media < 7.5:
    conceito = 'C'
    print('Aluno passou com nota: ',conceito)
elif media >= 4.0 and media < 6.0:
    conceito = 'D'
    print('Aluno reprovado com nota: ',conceito)
elif media <= 4.0 and media >= 0:
    conceito = 'E'
    print('Aluno reprovado com nota: ',conceito)
else:
    print('Erro, verifique os dados novamente!')
