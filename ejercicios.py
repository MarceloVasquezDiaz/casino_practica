import random
import time
import math

baraja = []

# Definir los palos de la baraja
pintas = ['corazones', 'diamantes', 'tréboles', 'picas']

# Definir los valores numéricos y las representaciones correspondientes
numeros_letras = [
    {'numero_letra': '2', 'valor': 2},
    {'numero_letra': '3', 'valor': 3},
    {'numero_letra': '4', 'valor': 4},
    {'numero_letra': '5', 'valor': 5},
    {'numero_letra': '6', 'valor': 6},
    {'numero_letra': '7', 'valor': 7},
    {'numero_letra': '8', 'valor': 8},
    {'numero_letra': '9', 'valor': 9},
    {'numero_letra': '10', 'valor': 10},
    {'numero_letra': 'J', 'valor': 10},
    {'numero_letra': 'Q', 'valor': 10},
    {'numero_letra': 'K', 'valor': 10},
    {'numero_letra': 'A', 'valor': 11},  # El As puede ser 1 u 11, pero en este caso lo consideramos 11
]

# Crear todas las cartas combinando palos y números/letras
for pinta in pintas:
    for numero_letra in numeros_letras:
        carta = {
            'valor': numero_letra['valor'],
            'pinta': pinta,
            'numero_letra': numero_letra['numero_letra']
        }
        baraja.append(carta)


mano = []
manoCrupier =[]
comprobador = True


def repartoInicial():
    '''
    Saca 2 cartas de la baraja y las da a la mano, tambien da dos cartas al crupie
    '''
    for i in range(2):
        valor = random.randint(0,len(baraja))
        tuCarta = baraja[valor]
        mano.append(tuCarta)
        baraja.remove(tuCarta)
        cartaCrupie = baraja[random.randint(0,len(baraja))]
        manoCrupier.append(cartaCrupie)
        baraja.remove(cartaCrupie)

def mostrarMano():
    for i in range(len(mano)):
        print(f'Tus cartas son {mano[i]['numero_letra']} de {mano[i]['pinta']}')
        time.sleep(0.5)
    print(f'La carta del Crupier es {mano[0]['numero_letra']} de {mano[0]['pinta']}')

def mostrarTodaLaMano():
    for i in range(len(mano)):
        print(f'Tus cartas son {mano[i]['numero_letra']} de {mano[i]['pinta']}')
        time.sleep(0.5)
    for j in range(len(manoCrupier)):
        print(f'Tus cartas son {manoCrupier[j]['numero_letra']} de {manoCrupier[j]['pinta']}')
        time.sleep(0.5)

def blackJack(x):
    if (x[0]['numero_letra'] == 'A' and x[1]['valor'] == 10) or (x[1]['numero_letra'] == 'A' and x[0]['valor'] == 10):
        print(f'Es blackjack de {x}')
        
        
def twentyone():
    if mano[0]['valor'] + mano[1]['valor'] <= 21:
        comprobador = True
    else:
        comprobador = False
        
def hit():
    valor = random.randint(0,len(baraja))
    tuCarta = baraja[valor]
    mano.append(tuCarta)
    baraja.remove(tuCarta)
    mostrarMano()

def sumavalor(x):
    key = 0
    for i in range(len(x)):
        key += x[i]['valor']
    return key

def quienGana():
    numeroJugador = sumavalor(mano)
    numeroCrupier = sumavalor(manoCrupier)
    
    if numeroJugador == numeroCrupier:
        print('Empate')
        mostrarTodaLaMano()
    elif numeroCrupier > 21 and numeroJugador <= 21:
        print('Haz ganado')
        mostrarTodaLaMano()
    elif numeroCrupier < numeroJugador < 21:
        print('Haz ganado')
        mostrarTodaLaMano()
    else:
        print('Perdiste')
        mostrarTodaLaMano()
    
def menu():
    value = int(input('Elige el número de la siguiente opciones: \n1.- Hit \n2.- Stand'))
    if value == 1:
        hit()
        valor = input('Desea seguir? 1.-Sí 2.-No')
        if valor == 'Sí':
            hit()
            valor = input('Desea seguir? 1.-Sí 2.-No')
        else:
            quienGana()
    else:
        quienGana()

repartoInicial()
mostrarMano()
menu()
