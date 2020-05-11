import os
import time
import re

# Animales: perro, gato, pez, serpiente y araña
# Perros-Perfil: semental, mascota, perro policía, apoyo a invidentes
# Gato-Color de Ojos: azules, verdes, negros, cafés, grises
# Pez-tipo de agua: dulce o salada
# Funciones: perro.semental.ladrar(), perro.mascota.dormir(), perro.policia.olfatear(), perro.apoyo_invidentes.sentarse()
regex_numero_int_decimal = '^([1-9]\d*(\.)\d*|0?(\.|\,)\d*[1-9]\d*|[1-9]\d*)$'
regex_nombre = '(\w+\s*)+' #TODO Validar a detalle esta variable
animal = []
# estructura del diccionario que guarara cada animal servira igualmente para tratar el archivo csv
SCHEMA = {
    'ID': {
        'type': 'autoincrement',
    },
    'ANIMAL': {
        'type': 'string',
        'max_length': 50
    },
    'PRECIO': {
        'type': 'float',
    },
    'NOMBRE': {
        'type': 'string',
        'max_length': 50
    },
    'RAZA': {
        'type': 'string',
        'max_length': 50
    },
    'EDAD': {
        'type': 'int'
    },
    'COLOR': {
        'type': 'string',
        'max_length': 50
    },
    'MOD_REPRODUCCION': {
        'type': 'string',
        'max_length': 50
    },
    'ALIMENTACION': {
        'type': 'string',
        'max_length': 50
    },
    'TAMANO': {
        'type': 'float'
    },
    'PESO': {
        'type': 'float'
    },
    'SEXO': {
        'type': 'string',
        'max_length': 6
    },
    'PERFIL': {
        'type': 'string',
        'max_length': 20
    },
    'COLOR_OJOS': {
        'type': 'string',
        'max_length': 15
    },
    'TIPO_AGUA': {
        'type': 'string',
        'max_length': 6
    },
    'PAIS_ORIGEN': {
        'type': 'string',
        'max_length': 15
    },
    'VENENOSO': {
        'type': 'string',
        'max_length': 2
    },
    'ESTADO_VENTA': {
        'type': 'string',
        'max_length': 6

    },
    'FUNCION': {
        'type': 'string',
        'max_length': 15
    }
}
''''              Validaciones                  '''


def validaString_Cadena(cadena):
    if not re.search(regex_nombre, cadena):
        raise ValueError(
            # f'El {parametro} ingresado debe tener como mínimo 3 caractares y un máximo de 50 caracteres, tamaño actual: {len(cadena)}')
            f'{cadena} no es un nombre valido')
    return True

def validarPrecio(precio):
    if float(precio) < 100:
        raise ValueError('El costo debe ser mayor a 100')
    return True

def validarNumero(cadena):
    if not re.search(regex_numero_int_decimal, cadena):
        raise ValueError(
            f'{cadena} no es un numero valido')

    return True


def check_nombre():
    print("Introduce el nombre")
    name = input()
    try:
        validaString_Cadena(name)
        return name
    except ValueError as err:
        print(err)
        check_nombre()

def check_precio():
    print("Ingresa el monto")
    precio = input()
    try:
        validarNumero(precio)
        if validarPrecio(precio):
            return precio
    except ValueError as err:
        print(err)
        check_precio()


def check_raza():
    print("Ingresa la raza")
    raza = input()
    try:
        validaString_Cadena(raza)
        return raza
    except ValueError as err:
        print(err)
        check_raza()


def check_edad():
    print('Ingresa la edad')
    edad = input()
    try:
        validarNumero(edad)
        return edad
    except ValueError as err:
        print(err)
        check_edad()


def check_color():
    print('Ingresa el color')
    color =input()
    try:
        validaString_Cadena(color)
        return color
    except ValueError as err:
        print(err)
        check_color()


def check_mod_reproduccion():
    pass


def check_tamano():
    print('Introduce el tamaño')
    tamano = input()
    try:
        validarNumero(tamano)
        return tamano
    except ValueError as err:
        print(err)
        check_tamano()


def comprarAnimal():
    print('Menu de Compra')
    print('*' * 50)
    print('Que tipo de Animal se va a comprar?')
    print('Selecciona una Opcion: ')
    print('[1]Perro')
    print('[2]Gato')
    print('[3]Pez')
    print('[4]Serpiente')
    print('[5]Araña')
    print('[V]olver')
    command = input()
    command = command.upper()
    if command == '1':
        #perros
        print('Perros')
        precio = check_precio()
        print(f'precio: {precio}')#verificar que el precio sea mayor o = 100
        nombre = check_nombre()
        print(f'nombre: {nombre}')
        raza = check_raza()
        print(f'raza: {raza}')
        edad = check_edad()#verificar que la edad sea mayo que cero
        print(f'edad: {edad}')
        color = check_color()
        print(f'color: {color}')
        mod_reprocuccion = 'Vivíparo'
        print(f'Modo de reproduccion: {mod_reprocuccion}')
        alimentacion = 'Omnívoro'
        print(f'Modo de reproduccion: {alimentacion}')
        tamano = check_tamano()
        print(f'Tamano: {tamano}')

#https://cosasdedevs.com/posts/como-crear-un-crud-en-python-parte-2-creacion-y-listado/

    elif command == '2':
        print(f'opcion {command}')
    elif command == '3':
        print(f'opcion {command}')
    elif command == '4':
        print(f'opcion {command}')
    elif command == '5':
        print(f'opcion {command}')
    elif command == 'V':
        print(f'opcion {command}')
    else:
        print('Comando inválido')



def print_options():
    print('Bienvenido a +Kota')
    print('*' * 50)
    print('Selecciona una opción:')
    print('[C]omprar Animal')
    print('[L]istado de Animales')
    print('[V]ender Animal')
    print('[E]liminar Animal')
    print('[B]uscar Animal')
    print('[S]ALIR')


def run():
    print_options()

    command = input()
    command = command.upper()

    if command == 'C':
        comprarAnimal()
    elif command == 'L':
        pass
    elif command == 'V':
        pass
    elif command == 'E':
        pass
    elif command == 'B':
        pass
    elif command == 'S':
        os._exit(1)
    else:
        print('Comando inválido')
        time.sleep(1)
        run()


if __name__ == "__main__":
    run()
