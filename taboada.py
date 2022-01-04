from time import sleep

print(f"{'-' * 20} \n{' ' :7}Tabuada \n{'-' * 20}")
while True:
    n = int(input('Digite número entre 1 e 10 para a tabuada \nou outro para encerrar: '))
    if n not in range(1, 11):
        break
    for x in range(1, 11):
        print(f'{n} x {x:2} = {n * x}')
        sleep(.5)
    print('-' * 20)

