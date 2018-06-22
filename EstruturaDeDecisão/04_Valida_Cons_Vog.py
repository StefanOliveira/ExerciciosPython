#Valida Letra - Consoante ou Vogal

aValLtr = input('Informe uma letra: ').upper()

if ('AEIOU'.find(aValLtr) >= 0):
    print ('A letra',aValLtr,'é uma vogal!')
else:
    print ('A letra',aValLtr,'é uma consoante!')
