from random import choice
print('\033[35m===========================\033[m')
print('\033[35m          sorteio\033[m')
print('\033[35m===========================\033[m')

motivo = input('\033[36mO sorteio será designado para: ')

c1 = input('Primeiro candidato: ')
c2 = input('Segundo candidato: ')
c3 = input('Terceiro candidato: ')
c4 = input('Quarto candidato: \033[m')

print(f'E o sorteado é: {choice([c1, c2, c3, c4])}')
