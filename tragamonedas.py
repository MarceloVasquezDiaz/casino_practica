# Tragamonedas consiste en tres rollos con distintas caras, para ganar deben ser las tres caras iguales
import random
import time

# Rollos
rollo1 = ['🍋', '🍉', '🍒', '🍑', '💎', '🍆', '💖', '🍌']
rollo2 = ['🍋', '🍉', '🍒', '🍑', '💎', '🍆', '💖', '🍌']
rollo3 = ['🍋', '🍉', '🍒', '🍑', '💎', '🍆', '💖', '🍌']

# Fondos
billetera = 150000
nombre = 'Nao'
creditos = 0

# Tabla de multiplicadores
# Limon 1000
# Sandía 2000
# Cereza 3000
# Durazno 5000
# Diamante 7000
# Berenjena 10000
# Coraazon 20000
# Platano 100000

def tirar_palanca():
    print('*Los rodillos comienzan a girar*')
    valor_maquina = random.randint(0 , 100)
    if valor_maquina == 100:
        time.sleep(0.5)
        print('|🍌|🍌|🍌|')
        print('Felicidades haz sacado el premio mayor $100.000')
        return 100000
    elif valor_maquina >= 98:
        time.sleep(0.5)
        print('|💖|💖|💖|')
        print('Felicidades haz sacado un excelente premio $20.000')
        return 20000
    elif valor_maquina >= 95:
        time.sleep(0.5)
        print('|🍆|🍆|🍆|')
        print('Felicidades haz sacado un grandiozo premio $10.000')
        return 10000
    elif valor_maquina >= 90:
        time.sleep(0.5)
        print('|💎|💎|💎|')
        print('Felicidades haz sacado un granpremio $7.000')
        return 7000
    elif valor_maquina >= 85:
        time.sleep(0.5)
        print('|🍑|🍑|🍑|')
        print('Felicidades haz sacado un muy buen premio $5.000')
        return 5000
    elif valor_maquina >= 78:
        time.sleep(0.5)
        print('|🍒|🍒|🍒|')
        print('Felicidades haz sacado un buen premio $3.000')
        return 3000
    elif valor_maquina >= 65:
        time.sleep(0.5)
        print('|🍉|🍉|🍉|')
        print('Felicidades haz sacado un premio $2.000')
        return 2000
    elif valor_maquina >= 40:
        time.sleep(0.5)
        print('|🍋|🍋|🍋|')
        print('Felicidades haz sacado un premio regular $1.000')
        return 1000
    else:
        eleccion_mala1 = random.choice(rollo1)
        eleccion_mala2 = random.choice(rollo1)
        eleccion_mala3 = random.choice(rollo3)
        while eleccion_mala1 == eleccion_mala2:
            eleccion_mala1 = random.choice(rollo1)
        else:
            time.sleep(0.5)
            print(f'|{eleccion_mala1}|{eleccion_mala2}|{eleccion_mala3}|')
            print('lo siento haz perdido')
        return 0
def anadir_creditos(billetera, creditos):
    print(f'{nombre} por favor ingrese cuanto creditos desea añadir cada uno tiene el valor de 1000, su saldo actual es de ${billetera}')
    precreditos = int(input('Ingrese el numero de creditos: '))
    if (precreditos * 1000) <= billetera:
        billetera -=  precreditos*1000
        creditos += precreditos
    else:
        print('Excede su billetera.')
    
    return billetera, creditos

# Loop de juego
while True:
    if creditos == 0:
        print(f'{nombre} no cuenta con creditos para jugar. Debe añadir creditos.')
        billetera, creditos = anadir_creditos(billetera, creditos)
        print(f'Cuenta con {creditos}')  
    if creditos > 0:
        print('Digite el numero de tiradas que desea realizar.')
        tiradas = int(input('Digite el numero: '))
        if tiradas <= creditos:
            for i in range(tiradas):
                creditos -= 1
                ganancia = tirar_palanca()
                time.sleep(0.5)
                billetera += ganancia
                print()
            print(f'{nombre} tu nuevo saldo es ${billetera}.')
            
        else:
            print('No cuenta con ese número de creditos.')
            
