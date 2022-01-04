lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    cont = input('Deseja continuar? [S/N]: ').upper()
    while cont not in 'SN':
        cont = input('Deseja continuar? [S/N]: ').upper()
    if cont == 'N':
        break
print(lista)
for c, v in enumerate(lista):
    if v % 2 ==0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Pares: {pares} \nÍmpares: {impares}')
