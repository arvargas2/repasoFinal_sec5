import os
import time
import numpy as np
import funciones_medicas as fm
# -------------- VARIABLES -----------------
opcion = ""   # Selección del usuario
tamaño = 2    # Cantidad máxima de pacientes
rut = ""      # Rut del paciente
arr_ruts = np.empty(tamaño, dtype=object)
nombre = ""   # Nombre del paciente
arr_nombres = np.empty(tamaño, dtype=object)
edad = 0      # Edad del paciente
arr_edades = np.empty(tamaño, dtype=int)
# -----------CÓDIGO PRINCIPAL-----------------
while True:
    os.system("cls")
    opcion = str(input('''
    --------- MENÚ -----------
    1.- Cargar datos
    2.- Buscar a un paciente por su rut 
    3.- Listar paciente menores de edad
    4.- Salir                     
    \n Elija opción: '''))

    if opcion == "1":
        os.system("cls")
        print("\n--------- CARGAR DATOS---------")
        for k in range(tamaño):
            rut = str(input("Ingrese rut:")).strip().upper()
            while not (fm.validar_rut(rut)):
                print("Error, no puede ser vacio")
                rut = str(input("Ingrese rut:")).strip().upper()
            arr_ruts[k] = rut
            
            nombre=str(input("Ingrese nombre:")).strip()
            while not (fm.validar_nombre(nombre)):
                print("Error, mínimo 3 caracteres")
                nombre=str(input("Ingrese nombre:")).strip()
            arr_nombres[k]=nombre
            
            edad=int(input("Ingrese edad: "))
            while not (fm.validar_edad(edad)):
                print("Error, mayor o igual a cero")    
                edad=int(input("Ingrese edad: "))
            arr_edades[k]=edad
                
            fm.imprimir_ficha_medica(rut, nombre,edad)     

        os.system("pause")
    if opcion == "2":
        os.system("cls")
        print("\n---- Buscar paciente por RUT ----")
        rut = str(input("Ingrese rut a buscar:")).strip().upper()
        if rut in arr_ruts:
            # Solo sabemos que esta almacenado, ahora debemos
            # determinar en que posición
            # >>>ARREGLAR ESTO CON UNA VARIABLE FLAG!!!!!!!!!!!!!<<<
            for k in range(tamaño):
                if rut == arr_ruts[k]:
                    posicion=k
            fm.imprimir_ficha_medica(arr_ruts[k],arr_nombres[k], arr_edades[k])                        
        else:
            print("NO esta!!!!")                            
        os.system("pause")
        
    if opcion == "3":
        os.system("cls")

        os.system("pause")
        
        
    if opcion == "4":
        break
