#Programa para leitura de 2 notas parciais e imprimir média

aNome = input('Digite o nome do Aluno: ')
nNot1 = float(input('Digite a primeira nota: '))
nNot2 = float(input('Digite a segunda nota: '))

nMedia = (nNot1 + nNot2) / 2
print('Media:',nMedia)

if nMedia >= 7:
    print('Aluno',aNome,'Aprovado!')
elif nMedia < 7:
    print('Aluno',aNome,'Reprovado!')
elif nMedia == 10:
    print('Aluno',aNome,'Aprovado com distinção!')
else:
    print('Erro, digite os dados novamente!')


