from random import randint
ganho = 0
while True:
    robo = randint(1, 5)
    jog = int(input('Jogue um número: '))
    poi = ' '
    while poi not in 'PI':
        poi = input('Par ou Impar [P/I]: ').strip().upper()

    print(f'Robo: {robo}. Resultado: {robo + jog}',end=' → ')
    if (robo + jog) % 2 == 0:
        resposta = 'P'
        resp = 'Par'
    else:
        resposta = 'I'
        resp = 'Impar'
    if poi == resposta:
        print(f'{resp}\nVenceu! Vamos jogar de novo!')
        ganho += 1
        print('=-' * 10)
    else:
        print(f'{resp} \nPerdeu! Ganhou ao todo {ganho} vezes.')
        break
