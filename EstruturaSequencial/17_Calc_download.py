#Calculadora - Tempo para Download

#Tamanho do arquivo a ser baixado
tArqDown = float(input('Digite o tamanho do arquivo para download: '))

#Link de internet - Velocidade de Conexão
tVelLink = float(input('Digite a velocidade de sua conexão: '))

#Tamanho total do arquivo
tArqBits = tArqDown * 1024 * 1024 * 8

#Calculo do tempo para transferência
tTmpSec = tArqBits / (tVelLink * 1024 * 1024)
tTmpMin = tTmpSec / 60

print ('Tempo estimado para download do ',tArqDown,' é de: {:.2f}'.format(tTmpMin),'minutos')
