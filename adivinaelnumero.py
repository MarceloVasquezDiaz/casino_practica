import random

numerosecreto = random.randint(1,20)
print(numerosecreto)
intento = 0
for intento in range(1, 7):
    print('Adivina el numero:')
    var = int(input())
    if var < numerosecreto:
        print('El numero es mayor al numero que estoy pensando.')
    elif var > numerosecreto:
        print('El numero es menor al numero que estoy pensando.')
    else:
        intento = var
        break

if intento == numerosecreto:
    print(f'Wena le achuntaste es {numerosecreto}')
else:
    print(f'No pudiste el numero era {numerosecreto}')