#Valida preço dos produtos e opta pelo mais barato

#Validar preço 1
valid_preco = False

while valid_preco == False:
    preco1 = input('Digite o preço do produto: ')
    try:
        preco1 = float(preco1)
        if preco1 <= 0:
            print('Valor do produto inválido.')
        else:
            valid_preco = True
    except:
        print("Formato de preço inválido, use apenas números separados por '.'.")

#Validar preço 2
valid_preco = False

while valid_preco == False:
    preco2 = input('Digite o preço do produto: ')
    try:
        preco2 = float(preco2)
        if preco2 <= 0:
            print('Valor do produto inválido.')
        else:
            valid_preco = True
    except:
        print("Formato de preço inválido, use apenas números separados por '.'.")

#Validar preço 3
valid_preco = False

while valid_preco == False:
    preco3 = input('Digite o preço do produto: ')
    try:
        preco3 = float(preco3)
        if preco1 <= 0:
            print('Valor do produto inválido.')
        else:
            valid_preco = True
    except:
        print("Formato de preço inválido, use apenas números separados por '.'.")

print('\nValidação de números em andamento!\n')

#Validando o maior número
if(preco1 == preco2) and (preco1 == preco3):
    print('Os preços são iguais!')
elif(preco1 < preco2) and (preco1 < preco3):
    print('O produto 1 tem o menor valor: R$',preco1)
elif(preco2 < preco3):
    print('O produto 2 tem o menor valor: R$',preco2)
else:
    print('O produto 3 tem o menor valor: R$',nNum3)


