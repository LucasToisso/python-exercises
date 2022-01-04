from random import randint
#import emoji

print((f'''\033[30m{'='*21}\033[m\n\033[30m{' '*4}Jogo da sorte\033[m\n\033[30m{'='*21}\033[m'''))
robo = randint(0, 10)
jogador = int(input('Em qual número eu pensei? '))
e = 0

while jogador != robo:
    e += 1
    if jogador < robo:
        print('Mais...')
    else:
        print('Menos...')
    jogador = int(input('Em qual número eu pensei? '))
print(f'Você errou {e} vezes, mas agora foi. Escolhi o número {robo}!')
