from time import sleep
from random import randint

jogador = int(input('''[1] Pedra
[2] Papel
[3] Tesoura
Escolha uma das opções:
'''))

robo = randint(1, 3)
print('JO')
sleep(.5)

print('KEN')
sleep(.5)

print('PO!!')
sleep(1)

if jogador == 1:
    print('Jogador: Pedra')
if jogador == 2:
    print('Jogador: Papel')
if jogador == 3:
    print('Jogador: Tesoura')

if jogador < 1 or jogador > 3:
    print('Erro!! Escolha uma das opções acima!!')
elif robo == 1:
    print('Robo: pedra')
elif robo == 2:
    print('Robo: papel')
else:
    print('Robo: tesoura')

if jogador == 1 and robo == 1:#PEDRA
    print('EMPATE: os dois escolheram pedra!')
elif jogador == 1 and robo == 2:
    print('PERDEU: pedra perde para papel!')
elif jogador == 1 and robo == 3:
    print('GANHOU: pedra ganha da tesoura!')

if jogador == 2 and robo == 2:#PAPEL
    print('EMPATE: os dois escolheram papel!')
elif jogador == 2 and robo == 3:
    print('PERDEU: papel perde para tesoura!')
elif jogador == 2 and robo == 1:
    print('GANHOU: papel ganha da pedra!')

if jogador == 3 and robo == 3:#TESOURA
    print('EMPATE: os dois escolheram tesoura!')
elif jogador == 3 and robo == 1:
    print('PERDEU: tesoura perde para pedra!')
elif jogador == 3 and robo == 2:
    print('GANHOU: tesoura ganha do papel!')
