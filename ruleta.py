import random
import time

ruleta = [
    {'Numero': '00', 'Color': 'Verde'},
    {'Numero': '27', 'Color': 'Rojo'}, 
    {'Numero': '10', 'Color': 'Negro'},
    {'Numero': '25', 'Color': 'Rojo'},
    {'Numero': '29', 'Color': 'Negro'},  
    {'Numero': '12', 'Color': 'Rojo'},
    {'Numero': '8', 'Color': 'Negro'},
    {'Numero': '19', 'Color': 'Rojo'},
    {'Numero': '31', 'Color': 'Negro'},
    {'Numero': '18', 'Color': 'Rojo'},
    {'Numero': '6', 'Color': 'Negro'},
    {'Numero': '21', 'Color': 'Rojo'},
    {'Numero': '33', 'Color': 'Negro'},  
    {'Numero': '16', 'Color': 'Rojo'},
    {'Numero': '4', 'Color': 'Negro'},
    {'Numero': '23', 'Color': 'Rojo'},
    {'Numero': '35', 'Color': 'Negro'}, 
    {'Numero': '14', 'Color': 'Rojo'},
    {'Numero': '2', 'Color': 'Negro'},
    {'Numero': '0', 'Color': 'Verde'},
    {'Numero': '28', 'Color': 'Negro'},  
    {'Numero': '9', 'Color': 'Rojo'},
    {'Numero': '26', 'Color': 'Negro'},  
    {'Numero': '30', 'Color': 'Rojo'},  
    {'Numero': '11', 'Color': 'Negro'},
    {'Numero': '7', 'Color': 'Rojo'},
    {'Numero': '20', 'Color': 'Negro'},
    {'Numero': '32', 'Color': 'Rojo'},  
    {'Numero': '17', 'Color': 'Negro'},
    {'Numero': '5', 'Color': 'Rojo'},
    {'Numero': '22', 'Color': 'Negro'},
    {'Numero': '34', 'Color': 'Rojo'},  
    {'Numero': '15', 'Color': 'Negro'},
    {'Numero': '3', 'Color': 'Rojo'},
    {'Numero': '24', 'Color': 'Negro'},  
    {'Numero': '36', 'Color': 'Rojo'},  
    {'Numero': '13', 'Color': 'Negro'},
    {'Numero': '1', 'Color': 'Rojo'}
]
apuesta = {}
numero_final = {}

def tirar_la_bola():
    print('Tirando con fuerza la ruleta y la bola el numero es...')
    for i in range(3):
        print('*')
        time.sleep(0.5)
    numero_final = random.choice(ruleta)
    print(f'el numero es el {numero_final['Numero']} {numero_final['Color']}')
    return numero_final

# Tipos de apuesta internas

def apuesta_plana():
    apuesta['Fichas'] *= 36
    if numero_final['Numero'] == apuesta['Numero']:
        return True, apuesta
    return False

def apuesta_dividida():
    apuesta['Fichas'] *= 18
    if numero_final['Numero'] in apuesta['Numero']:
        return True, apuesta
    return False

def apuesta_calle():
    apuesta['Fichas'] *= 12
    if numero_final['Numero'] in apuesta['Numero']:
        return True, apuesta
    return False

def apuesta_esquina():
    apuesta['Fichas'] *= 9
    if numero_final['Numero'] in apuesta['Numero']:
        return True, apuesta
    return False

def apuesta_linea():
    apuesta['Fichas'] *= 6
    if numero_final['Numero'] in apuesta['Numero']:
        return True, apuesta
    return False

# Tipos de apuesta externas
def apuesta_color():
    apuesta['Fichas'] *= 2
    if numero_final['Color'] == apuesta['Color']:
        return True, apuesta
    return False

def apuesta_par_impar():
    apuesta['Fichas'] *= 2
    if numero_final['Numero'] in apuesta['Numero']:
        return True, apuesta
    return False

def apuesta_alta_baja():
    apuesta['Fichas'] *= 2
    if numero_final['Numero'] in apuesta['Numero']:
        return True, apuesta
    return False

def apuesta_docena():
    apuesta['Fichas'] *= 3
    if numero_final['Numero'] in apuesta['Numero']:
        return True, apuesta
    return False

def apuesta_columnas():
    apuesta['Fichas'] *=3
    if numero_final['Numero'] in apuesta['Numero']:
        return True, apuesta
    return False

def eleccion_apuesta():
    print('Tipos de apuestas \n1. Apuesta Plana. \n2. Apuesta dividia. \n3. Apuesta calle. \n4. Apuesta esquina. \n5. Apuesta linea. \n6. Apuesta color. \n7. Apuesta Par o Impar. \n8. Apuesta alta o baja. \n9. Apuesta docena \n10. Apuesta Columna')
    key = int(input('Ingrese el número de su tipo de apuesta: '))
    match key:
        case 1:
            apuesta['Fichas'] = int(input('Ingrese la apuesta que desea: '))
            apuesta['Numero'] = input('Ingrese su numero: ')
            return apuesta, 1
        case 2:
            apuesta['Fichas'] = int(input('Ingrese la apuesta que desea: '))
            lista = [input('Ingrese valor: ') for _ in range(2)]
            apuesta['Numero'] = lista
            return apuesta, 2
        case 3:
            apuesta['Fichas'] = int(input('Ingrese la apuesta que desea: '))
            lista = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['10', '11', '12'], ['13', '14', '15'], ['16', '17', '18'], ['19', '20', '21'], ['22', '23', '24'], ['25', '26', '27'], ['28', '29', '30'], ['31', '32', '33'], ['34', '35', '36']]
            i = int(input('Elija una calle: \n1.-[1|2|3] \n2.-[4|5|6] \n3.-[7|8|9] \n4.-[10|11|12] \n5.-[13|14|15] \n6.-[16|17|18] \n7.-[19|20|21] \n8.-[22|23|24] \n9.-[25|26|27] \n10.-[28|29|30] \n11.-[31|32|33] \n12.-[34|35|36]')) - 1
            apuesta['Numero'] = lista[i]
            return apuesta, 3
        case 4:
            apuesta['Fichas'] = int(input('Ingrese la apuesta que desea: '))
            lista = [input('Ingrese valor: ') for _ in range(4)]
            apuesta['Numero'] = lista
            return apuesta, 4
        case 5:
            apuesta['Fichas'] = int(input('Ingrese la apuesta que desea: '))
            lista = [['1', '2', '3', '4', '5', '6'], ['7', '8', '9','10', '11', '12'], ['13', '14', '15','16', '17', '18'], ['19', '20', '21' ,'22', '23', '24'], ['25', '26', '27', '28', '29', '30'], ['31', '32', '33', '34', '35', '36']]
            i = int(input('Elija una calle: \n1.-[1|2|3][4|5|6] \n2.-[7|8|9][10|11|12] \n3.-[13|14|15][16|17|18] \n4.-[19|20|21][22|23|24] \n5.-[25|26|27][28|29|30] \n6.-[31|32|33][34|35|36]\n')) - 1
            apuesta['Numero'] = lista[i]
            return apuesta, 5
        case 6:
            apuesta['Fichas'] = int(input('Ingrese la apuesta que desea: '))
            apuesta['Color'] = input('Escriba el color Negro o Rojo\n').capitalize()
            return apuesta, 6
        case 7:
            apuesta['Fichas'] = int(input('Ingrese la apuesta que desea: '))
            lista = [[str(x) for x in range(1, 37) if x%2 != 0], [str(x) for x in range(1, 37) if x%2 == 0]]
            apuesta['Numero'] = lista[int(input('Ingrese 1.- Impar o 2.- Par\n')) - 1]
            return apuesta, 7
        case 8:
            apuesta['Fichas'] = int(input('Ingrese la apuesta que desea: '))
            lista = [[str(x) for x in range(1, 19)], [str(x) for x in range(19, 37)]]
            apuesta['Numero'] = lista[int(input('Ingrese 1.- Del 1 al 18 o 2.- Del 19 al 36\n')) - 1]
            return apuesta, 8
        case 9:
            apuesta['Fichas'] = int(input('Ingrese la apuesta que desea: '))
            lista = [[str(x) for x in range(1, 13)], [str(x) for x in range(13, 25)], [str(x) for x in range(25, 37)]]
            apuesta['Numero'] = lista[int(input('Ingrese \n1.- Set 1-12 \n2.- Set 13-24 \n3.- Set 25-36\n')) - 1]
            return apuesta, 9
        case 10:
            apuesta['Fichas'] = int(input('Ingrese la apuesta que desea: '))
            lista = [[str(x) for x in range(1, 37) if (x - 1) % 3 == 0], [str(x) for x in range(1, 37) if (x - 2) % 3 == 0], [str(x) for x in range(1, 37) if (x - 3) % 3 == 0]]
            apuesta['Numero'] = lista[int(input('Ingrese \n1.- Columna 1 \n2.- Columna 2 \n3.- Columna 3\n')) - 1]
            return apuesta, 10

apuesta, valor = eleccion_apuesta()
print(apuesta)
numero_final = tirar_la_bola()
match valor:
    case 1:
        ganar = apuesta_plana()
        if ganar:
            print(f'Ganaste {apuesta['Fichas']}')
    case 2:
        ganar = apuesta_dividida()
        if ganar:
            print(f'Ganaste {apuesta['Fichas']}')
    case 3:
        ganar = apuesta_calle()
        if ganar:
            print(f'Ganaste {apuesta['Fichas']}')
    case 4:
        ganar = apuesta_esquina()
        if ganar:
            print(f'Ganaste {apuesta['Fichas']}')
    case 5:
        ganar = apuesta_linea()
        if ganar:
            print(f'Ganaste {apuesta['Fichas']}')
    case 6:
        ganar = apuesta_color()
        if ganar:
            print(f'Ganaste {apuesta['Fichas']}')
    case 7:
        ganar = apuesta_par_impar()
        if ganar:
            print(f'Ganaste {apuesta['Fichas']}')
    case 8:
        ganar = apuesta_alta_baja()
        if ganar:
            print(f'Ganaste {apuesta['Fichas']}')
    case 9:
        ganar = apuesta_docena()
        if ganar:
            print(f'Ganaste {apuesta['Fichas']}')
    case 10:
        ganar = apuesta_columnas()
        print(ganar)
        if ganar:
            print(f'Ganaste {apuesta['Fichas']}')