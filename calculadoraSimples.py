from time import sleep

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
m = 0
while m != 5:
    m = int(input('------- MENU ------- \n[1]Somar \n[2]Multiplicar \n[3]Maior \n[4]Novos números \n[5]Fim \nEscolha uma das opções: '))
    if m == 1:
        print(f'Soma: {n1} + {n2} = {n1 + n2}'), sleep(.5)
    elif m == 2:
        print(f'Multiplicação: {n1} x {n2} = {n1 * n2}'), sleep(.5)
    elif m == 3:
        print(f'Maior entre {n1} e {n2} é {max(n1, n2, 1)}'), sleep(.5)
    elif m == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
        sleep(.5)
    elif m == 5:
        print('Fim')
    else:
        print('Opção Inválida!'), sleep(.5)
