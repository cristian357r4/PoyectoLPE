import csv
import os
import time
import re
from prettytable import PrettyTable

# Animales: perro, gato, pez, serpiente y araña
# Perros-Perfil: semental, mascota, perro policía, apoyo a invidentes
# Gato-Color de Ojos: azules, verdes, negros, cafés, grises
# Pez-tipo de agua: dulce o salada
# Funciones: perro.semental.ladrar(), perro.mascota.dormir(), perro.policia.olfatear(), perro.apoyo_invidentes.sentarse()
regex_numero_int_decimal = '^([1-9]\d*(\.)\d*|0?(\.|\,)\d*[1-9]\d*|[1-9]\d*)$'
regex_nombre = '(([A-Za-z])\w+\s*)+'  # TODO Validar a detalle esta variable
animal = []
stock_Animales = []

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
    'FUNCION': {
        'type': 'string',
        'max_length': 15
    },
    'ESTADO_VENTA': {
        'type': 'string',
        'max_length': 6

    }
}
'''               Operaciones de Archivo            '''


def consultar_animales(): #consulta animaes retornando una lista
    print('Consultar todos')
    list_data = []
    list_header = []
    with open('animales.csv', mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        is_header = True
        for row in csv_reader:
            if is_header:
                list_header = row
                is_header = False
                continue
            if row:
                file = {}
                for key, value in enumerate(row):
                    file[list_header[key]] = value

                list_data.append(file)
    # diccionario de listas
    #stock_Animales = list_data
    #print(f'lista de animales temporal: {stock_Animales}')
    return list_data


def _print_table_animales(lista_animales):
    #lista original

    table = PrettyTable(SCHEMA.keys())
    index = 0
    while index < len(lista_animales):
        '''for key in list_contacts[index]:
            print(list_contacts[index][key])'''
        #print(f'(index,estado_venta) = ({index+1},',lista_animales[index]['ESTADO_VENTA'],')')
        table.add_row(list(lista_animales[index].values()))
        index += 1
    print(table)
    print('Pulsa cualquier letra para continuar')

    command = input()


def save_animal(animal):
    # animal es lista
    return insert(animal)


def insert(data):
    with open('animales.csv', mode='a', encoding='utf-8') as csv_file:
        data_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        data_writer.writerow(data)
    return True


'''def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return  arr'''

def buscar_animal():
    print('Buscar Registro')
    filters = {}
    print('Buscar por tipo de animal (vacío para usar otro filtro):')
    animal = input()
    if animal:
        filters['ANIMAL'] = animal
    print('Buscar por tipo de Alimentacion (vacío para usar otro filtro):')
    alimentacion = input()
    if alimentacion:
        filters['ALIMENTACION'] = alimentacion
    print('Buscar por tipo de Reproduccion (vacío para usar otro filtro):')
    reproduccion = input()
    if reproduccion:
        filters['MOD_REPRODUCCION'] = reproduccion
    try:
        print("Opcion Aun no implementada")
        print (f'Filters: {filters}')
        list_animales = search_animales(filters)
        if not list_animales:
            return print('No hay ningún registro con esos criterios de búsqueda')
        else:
            _print_table_animales(list_animales)
    except ValueError as err:
        print(err)
        time.sleep(1)
        buscar_animal()

def search_animales(filters):

    #filters diccionario
    if 'ANIMAL' not in filters and 'ALIMENTACION' not in filters and 'MOD_REPRODUCCION' not in filters:
        raise ValueError('Debes envíar al menos un filtro')

    list_animales = filtrar_resultados(filters)
    print(f'Lista de elementos filtrados {list_animales}')
    return list_animales


def filtrar_resultados(filters):

    list_data = []
    columnas = []
    with open('animales.csv', mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        is_header = True
        for row in csv_reader:
            if is_header:
                columnas = row
                is_header = False
                continue

            if row:
                file = {}

                for key, value in enumerate(row):
                    file[columnas[key]] = value

                for key_filter, value_filter in filters.items():
                    matches = re.search(rf"{value_filter}", file[key_filter], re.IGNORECASE)
                    if matches:
                        list_data.append(file)
                        break

    return list_data

# def resultados_de_busqueda(lista_animales):
#
#     if not lista_animales:
#         return None
#
#     object_contacts = []
#     # Convertimos los datos a objectos de tipo contact
#     for animal in lista_animales:
#         c = Contact(animal['ID'], animal['NAME'], animal['SURNAME'], animal['EMAIL'], animal['PHONE'], animal['BIRTHDAY'])
#         object_contacts.append(c)
#
#     return object_contacts

def get_last_id():
    list_ids = []
    with open('animales.csv', mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        is_header = True
        for row in csv_reader:
            if is_header:
                is_header = False
                continue
            if row:
                list_ids.append(row[0])
    #print('Before order: ', list_ids)
    #print(list_ids[-1])

    if not list_ids:
        return 0

    # Ordenamos la lista de mayor a menor y retornamos el elemento de mayor tamaño
    #    list_ids.sort(reverse=True)
    return int(list_ids[-1])


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
    while True:
        print("Introduce el nombre")
        name = input()
        try:
            validaString_Cadena(name)
            return name
        except ValueError as err:
            print(err)


def check_precio():
    while True:
        print("Ingresa el Precio")
        precio = input()
        try:
            validarNumero(precio)
            if validarPrecio(precio):
                return precio
        except ValueError as err:
            print(err)


def check_raza():
    while True:
        print("Ingresa la raza")
        raza = input()
        try:
            validaString_Cadena(raza)
            return raza
        except ValueError as err:
            print(err)


def validarEdad(edad):
    if float(edad) > 5:
        raise ValueError('La edad del perro supera el limite establecido que son 5 años')
    return True


def validarTamaño(tamano, animal):
    if animal == 'g':
        if float(tamano) < 12:
            raise ValueError('El gato es muy pequeño debe medir al menos 12 cm')
        return True
    elif animal == 's':
        if float(tamano) > 130:
            raise ValueError('La serpiente es demasiado grande, debe medir menos de 130 cm')
        return True
    elif animal == 'a':
        if float(tamano) > 12:
            raise ValueError('La araña es demasiado grande, debe medir menos de 12 cm')
        return True
    else:
        return True


def validaPeso(peso, animal):
    if animal == 'fish':
        if float(peso) >= 50:
            raise ValueError('El peso del pez debe ser menor a los 50 gramos')
        return True
    elif animal == 'spider':
        if float(peso) >= 500:
            raise ValueError('El peso de la araña debe ser menor de 500 gramos')
        return True
    else:
        return True


def check_edad():
    while True:
        print('Ingresa la edad')
        edad = input()
        try:
            validarNumero(edad)
            return edad
        except ValueError as err:
            print(err)


def check_edad_perro():
    while True:
        print('Ingresa la edad')
        edad = input()
        try:
            validarNumero(edad)
            if validarEdad(edad):
                return edad
        except ValueError as err:
            print(err)


def check_color():
    while True:
        print('Ingresa el color')
        color = input()
        try:
            validaString_Cadena(color)
            return color
        except ValueError as err:
            print(err)


def check_tamano(animal):
    while True:
        print('Introduce el tamaño en centimetros')
        tamano = input()
        try:
            validarNumero(tamano)
            if validarTamaño(tamano, animal):
                return tamano
        except ValueError as err:
            print(err)


def check_tamano_gato():
    while True:
        print('Introduce el tamaño en centimetros')
        tamano = input()
        try:
            validarNumero(tamano)
            if validarTamaño(tamano, 'g'):
                return tamano
        except ValueError as err:
            print(err)


def check_peso(animal):
    while True:
        print('Ingresa el peso en gramos')
        peso = input()
        try:
            validarNumero(peso)
            if validaPeso(peso, animal):
                return peso
        except ValueError as err:
            print(err)


def check_sexo():
    while True:
        print('Elige el sexo')
        print('[M]asculino')
        print('[F]emenino')
        sexo = input()
        sexo = sexo.upper()
        if sexo == 'M':
            return 'Masculino'
        elif sexo == 'F':
            return 'Femenino'
        else:
            print('Opcion no valida')
            time.sleep(1)


def check_perfil():
    while True:
        print('Elige el perfil')
        # Perros - Perfil: semental, mascota, perro policía, apoyo a invidentes
        print('[S]emental')
        print('[M]ascota')
        print('[P]olicia')
        print('[A]poyo para invidentes')
        perfil = input()
        perfil = perfil.upper()
        if perfil == 'S':
            return 'S'
        elif perfil == 'M':
            return 'M'
        elif perfil == 'P':
            return 'P'
        elif perfil == 'A':
            return 'A'
        else:
            print('Opcion Incorrecta')
            time.sleep(1)

    # Funciones: perro.semental.ladrar(), perro.mascota.dormir(), perro.policia.olfatear(), perro.apoyo_invidentes.sentarse()


def check_color_ojos_gato():
    while True:
        print('Selecciona el color de ojos')
        print('[A]zules')
        print('[V]erdes')
        print('[N]egros')
        print('[C]afés')
        print('[G]rises')
        eye_color = input()
        eye_color = eye_color.upper()
        if eye_color == 'A':
            return 'Azul'
        elif eye_color == 'V':
            return 'Verde'
        elif eye_color == 'N':
            return 'Negro'
        elif eye_color == 'C':
            return 'Café'
        elif eye_color == 'G':
            return 'Gris'
        else:
            print('Opcion Incorrecta')
            time.sleep(1)


def check_alimentacio():
    while True:
        print('Selecciona el tipo de Alimentacion')
        print('[O]mnivoro')
        print('[C]arnivoro')
        alimentacion = input()
        alimentacion = alimentacion.upper()
        if alimentacion == 'O':
            return 'Omnivoro'
        elif alimentacion == 'C':
            return 'Carnivoro'
        else:
            print('Opcion Incorrecta')
            time.sleep(1)


def check_type_agua():
    while True:
        print('Selecciona el tipo de Agua')
        print('[D]ulce')
        print('[S]alada')
        tipo_agua = input()
        tipo_agua = tipo_agua.upper()
        if tipo_agua == 'D':
            return 'Dulce'
        elif tipo_agua == 'S':
            return 'Salada'
        else:
            print('Opcion Incorrecta')
            time.sleep(1)


def check_pais_origen():
    while True:
        print('Ingrese el pais de Origen')
        pais_origen = input()
        try:
            validaString_Cadena(pais_origen)
            return pais_origen
        except ValueError as err:
            print(err)


def check_venenoso():
    while True:
        print('La araña es venenosa ?')
        print('[S]i')
        print('[N]o')
        venenoso = input()
        venenoso = venenoso.upper()
        if venenoso == 'S':
            return 'SI'
        elif venenoso == 'N':
            return 'NO'
        else:
            print('Opcion Incorrecta')
            time.sleep(1)


def comprarAnimal():
    # regresara el animal como una lista
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
    # perro
    if command == '1':
        # perros
        #obtener el ultimo ID
        indice = get_last_id() +1
        animal.append(indice)

        print('Perros')
        animal.append('Perro')

        precio = check_precio()
        animal.append(precio)
        print(f'Precio: {precio}')  # verificar que el precio sea mayor o = 100

        nombre = check_nombre()
        print(f'Nombre: {nombre}')
        animal.append(nombre)

        raza = check_raza()
        print(f'Raza: {raza}')
        animal.append(raza)

        edad = check_edad_perro()  # verificar que la edad sea mayo que cero
        print(f'Edad: {edad}')
        animal.append(edad)

        color = check_color()
        print(f'Color: {color}')
        animal.append(color)

        mod_reprocuccion = 'Vivíparo'
        print(f'Modo de reproduccion: {mod_reprocuccion}')
        animal.append(mod_reprocuccion)

        alimentacion = 'Omnívoro'
        print(f'Tipo de alimentacion: {alimentacion}')
        animal.append(alimentacion)

        tamano = check_tamano('p')
        print(f'Tamano: {tamano}')
        animal.append(tamano)

        peso = check_peso('perro')
        print(f'Peso: {peso}')
        animal.append(peso)

        sexo = check_sexo()
        print(f'Sexo {sexo}')
        animal.append(sexo)

        perfil = check_perfil()
        funcion = ''
        # perro.semental.ladrar(), perro.mascota.dormir(), perro.policia.olfatear(), perro.apoyo_invidentes.sentarse()
        if perfil == 'S':
            perfil = 'Semental'
            funcion = 'Ladrar'
        elif perfil == 'M':
            perfil = 'Mascota'
            funcion = 'Dormir'
        elif perfil == 'P':
            perfil = 'Policia'
            funcion = 'Olfatear'
        elif perfil == 'A':
            perfil = 'Apoyo a invidentes'
            funcion = 'Sentarse'
        print(f'Perfil: {perfil}')
        animal.append(perfil)

        color_ojo = 'N/A'
        print(f'Color de ojos: {color_ojo}')
        animal.append(color_ojo)

        tipo_agua = 'N/A'
        print(f'Tipo Agua: {tipo_agua}')
        animal.append(tipo_agua)

        pais_origen = 'N/A'
        print(f'Pais de Origen: {pais_origen}')
        animal.append(pais_origen)

        venenoso = 'N/A'
        print(f'Venenoso: {venenoso}')
        animal.append(venenoso)

        print(f'Funcion: {funcion}')
        animal.append(funcion)

        estado_venta = 1
        print(f'Estado de Venta: {estado_venta}')
        animal.append(estado_venta)
        #lista que se agregara al diccionario de animales
        #print(f'Lista de salida(renglon) = {animal}')
        #mandar lista
        save_animal(animal)

    # Gato
    elif command == '2':
        indice = get_last_id() + 1
        animal.append(indice)

        print('Gatos')
        animal.append('Gato')

        precio = check_precio()
        print(f'Precio: {precio}')  # verificar que el precio sea mayor o = 100
        animal.append(precio)

        nombre = check_nombre()
        print(f'Nombre: {nombre}')
        animal.append(nombre)

        raza = check_raza()
        print(f'Raza: {raza}')
        animal.append(raza)

        edad = check_edad()  # verificar que la edad sea mayo que cero
        print(f'Edad: {edad}')
        animal.append(edad)

        color = check_color()
        print(f'Color: {color}')
        animal.append(color)

        mod_reprocuccion = 'Vivíparo'
        print(f'Modo de Reproduccion: {mod_reprocuccion}')
        animal.append(mod_reprocuccion)

        alimentacion = 'Omnívoro'
        print(f'Modo de Alimentacion: {alimentacion}')
        animal.append(alimentacion)

        tamano = check_tamano_gato()
        print(f'Tamano: {tamano}')
        animal.append(tamano)

        peso = check_peso('gato')
        print(f'Peso: {peso}')
        animal.append(peso)

        sexo = check_sexo()
        print(f'Sexo {sexo}')
        animal.append(sexo)

        perfil = 'N/A'
        print(f'Perfil: {perfil}')
        animal.append(perfil)

        color_ojo = check_color_ojos_gato()
        print(f'Color de ojos: {color_ojo}')
        animal.append(color_ojo)

        tipo_agua = 'N/A'
        print(f'Tipo Agua: {tipo_agua}')
        animal.append(tipo_agua)

        pais_origen = 'N/A'
        print(f'Pais de Origen: {pais_origen}')
        animal.append(pais_origen)

        venenoso = 'N/A'
        print(f'Venenoso: {venenoso}')
        animal.append(venenoso)

        funcion = 'N/A'
        print(f'Funcion: {funcion}')
        animal.append(funcion)

        estado_venta = '1'
        print(f'Estado de Venta: {estado_venta}')
        animal.append(estado_venta)

        #print(f'Lista de salida(renglon) = {animal}')
        # mandar lista
        save_animal(animal)

    # pez
    elif command == '3':
        indice = get_last_id() + 1
        animal.append(indice)

        print('Pez')
        animal.append('Pez')

        precio = check_precio()
        print(f'Precio: {precio}')  # verificar que el precio sea mayor o = 100
        animal.append(precio)

        nombre = check_nombre()
        print(f'Nombre: {nombre}')
        animal.append(nombre)

        raza = check_raza()
        print(f'Raza: {raza}')
        animal.append(raza)

        edad = check_edad()  # verificar que la edad sea mayo que cero
        print(f'Edad: {edad}')
        animal.append(edad)

        color = check_color()
        print(f'Color: {color}')
        animal.append(color)

        mod_reprocuccion = 'Ovuliparo'
        print(f'Modo de Reproduccion: {mod_reprocuccion}')
        animal.append(mod_reprocuccion)

        alimentacion = check_alimentacio()
        print(f'Modo de Alimentacion: {alimentacion}')
        animal.append(alimentacion)

        tamano = check_tamano('f')
        print(f'Tamano: {tamano}')
        animal.append(tamano)

        peso = check_peso('fish')
        print(f'Peso: {peso}')
        animal.append(peso)

        sexo = check_sexo()
        print(f'Sexo {sexo}')
        animal.append(sexo)

        perfil = 'N/A'
        print(f'Perfil: {perfil}')
        animal.append(perfil)

        color_ojo = 'N/A'
        print(f'Color de ojos: {color_ojo}')
        animal.append(color_ojo)

        tipo_agua = check_type_agua()
        print(f'Tipo Agua: {tipo_agua}')
        animal.append(tipo_agua)

        pais_origen = 'N/A'
        print(f'Pais de Origen: {pais_origen}')
        animal.append(pais_origen)

        venenoso = 'N/A'
        print(f'Venenoso: {venenoso}')
        animal.append(venenoso)

        funcion = 'N/A'
        print(f'Funcion: {funcion}')
        animal.append(funcion)

        estado_venta = 1
        print(f'Estado de Venta: {estado_venta}')

        animal.append(estado_venta)

    # serpiente
    elif command == '4':
        indice = get_last_id() + 1
        animal.append(indice)

        print('Serpiente')
        animal.append('Serpiente')

        precio = check_precio()
        print(f'Precio: {precio}')  # verificar que el precio sea mayor o = 100
        animal.append(precio)

        nombre = check_nombre()
        print(f'Nombre: {nombre}')
        animal.append(nombre)

        raza = check_raza()
        print(f'Raza: {raza}')
        animal.append(raza)

        edad = check_edad()  # verificar que la edad sea mayo que cero
        print(f'Edad: {edad}')
        animal.append(edad)

        color = check_color()
        print(f'Color: {color}')
        animal.append(color)

        mod_reprocuccion = 'Oviparo'
        print(f'Modo de Reproduccion: {mod_reprocuccion}')
        animal.append(mod_reprocuccion)

        alimentacion = 'Carnivoro'
        print(f'Modo de Alimentacion: {alimentacion}')
        animal.append(alimentacion)

        tamano = check_tamano('s')
        print(f'Tamano: {tamano}')
        animal.append(tamano)

        peso = check_peso('serpiente')
        print(f'Peso: {peso}')
        animal.append(peso)

        sexo = check_sexo()
        print(f'Sexo {sexo}')
        animal.append(sexo)

        perfil = 'N/A'
        print(f'Perfil: {perfil}')
        animal.append(perfil)

        color_ojo = 'N/A'
        print(f'Color de ojos: {color_ojo}')
        animal.append(color_ojo)

        tipo_agua = 'N/A'
        print(f'Tipo Agua: {tipo_agua}')
        animal.append(tipo_agua)

        pais_origen = check_pais_origen()
        print(f'Pais de Origen: {pais_origen}')
        animal.append(pais_origen)

        venenoso = 'N/A'
        print(f'Venenoso: {venenoso}')
        animal.append(venenoso)

        funcion = 'N/A'
        print(f'Funcion: {funcion}')
        animal.append(funcion)

        estado_venta = 1
        print(f'Estado de Venta: {estado_venta}')
        animal.append(estado_venta)

        save_animal(animal)
    # arañas
    elif command == '5':
        indice = get_last_id() + 1
        animal.append(indice)

        print('Arañas')
        animal.append('Araña')

        precio = check_precio()
        print(f'Precio: {precio}')  # verificar que el precio sea mayor o = 100
        animal.append(precio)

        nombre = check_nombre()
        print(f'Nombre: {nombre}')
        animal.append(nombre)

        raza = check_raza()
        print(f'Raza: {raza}')
        animal.append(raza)

        edad = check_edad()  # verificar que la edad sea mayo que cero
        print(f'Edad: {edad}')
        animal.append(edad)

        color = check_color()
        print(f'Color: {color}')
        animal.append(color)

        mod_reprocuccion = 'Oviparo'
        print(f'Modo de Reproduccion: {mod_reprocuccion}')
        animal.append(mod_reprocuccion)

        alimentacion = 'Carnivoro'
        print(f'Modo de Alimentacion: {alimentacion}')
        animal.append(alimentacion)

        tamano = check_tamano('a')
        print(f'Tamano: {tamano}')
        animal.append(tamano)

        peso = check_peso('spider')
        print(f'Peso: {peso}')
        animal.append(peso)

        sexo = check_sexo()
        print(f'Sexo {sexo}')
        animal.append(sexo)

        perfil = 'N/A'
        print(f'Perfil: {perfil}')
        animal.append(perfil)

        color_ojo = 'N/A'
        print(f'Color de ojos: {color_ojo}')
        animal.append(color_ojo)

        tipo_agua = 'N/A'
        print(f'Tipo Agua: {tipo_agua}')
        animal.append(tipo_agua)

        pais_origen = 'N/A'
        print(f'Pais de Origen: {pais_origen}')
        animal.append(pais_origen)

        venenoso = check_venenoso()
        print(f'Venenoso: {venenoso}')
        animal.append(venenoso)

        funcion = 'N/A'
        print(f'Funcion: {funcion}')
        animal.append(funcion)

        estado_venta = 1
        print(f'Estado de Venta: {estado_venta}')
        animal.append(estado_venta)

        save_animal(animal)

    elif command == 'V':
        run()
    else:
        print('Comando inválido')
        time.sleep(1)
        comprarAnimal()


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
        #consulta animales
        _print_table_animales(consultar_animales())

    elif command == 'V':
        pass
    elif command == 'E':
        pass
    elif command == 'B':
        buscar_animal()
    elif command == 'S':
        os._exit(1)
    else:
        print('Comando inválido')
    time.sleep(1)
    run()


if __name__ == "__main__":
    run()
