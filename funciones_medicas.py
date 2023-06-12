import random

def validar_rut(rut):
    return len(rut.strip())>0

def validar_nombre(nombre):
    return len(nombre.strip())>=3

def validar_edad(edad):
    return edad>=0

def imprimir_ficha_medica(rut, nombre, edad):
    codigo = random.randint(1000,9999)
    print(f'''
    ----------- FICHA MEDICA --------------
    Código atención: {codigo}
    Rut: {rut}
    Nombre: {nombre}
    Edad: {edad} años  ''')