import random

num = 10
lista = list(range(num))+[7]*3

saldo = int(input('Ingrese saldo para jugar: '))
apuesta = int(input('Apuesta por juego: '))

while saldo>0:
    print(f'Saldo disponible: ${saldo}')
    if random.choice(lista) == int(input(f'Seleccione un numero del 1-{num}: ')):
        saldo+=apuesta
        print(f'Ganaste +${apuesta}')
    else:
        saldo-=apuesta
        print(f'Perdiste -${apuesta}')

print('Se agotó tu saldo')
