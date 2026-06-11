
# Programa principal: Gestion de convocatoria del Mundial

from dt import DT
from arquero import Arquero
from defensa import Defensa
from medio_campo import MedioCampo
from delantero import Delantero
from analisis import Analisis


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingrese un numero valido")




def leer_habilidad(mensaje):
    while True:
        valor = leer_entero(mensaje + " (1-100): ")
        if 1 <= valor <= 100:
            return valor
        print("El valor debe estar entre 1 y 100")


def leer_edad(mensaje):
    while True:
        valor = leer_entero(mensaje + " (1-40): ")
        if 1 <= valor <= 40:
            return valor
        print("El valor debe estar entre 1 y 40")


def datos_basicos():
    nombre = input("Nombre del jugador: ")
    dorsal = leer_entero("Dorsal: ")
    edad = leer_edad("Edad: ")
    return nombre, dorsal, edad


def registrar_arquero():
    nombre, dorsal, edad = datos_basicos()
    reflejos = leer_habilidad("Reflejos")
    posicionamiento = leer_habilidad("Posicionamiento")
    manejo = leer_habilidad("Manejo de balon")
    return Arquero(nombre, dorsal, edad, reflejos, posicionamiento, manejo)


def registrar_defensa():
    nombre, dorsal, edad = datos_basicos()
    marcaje = leer_habilidad("Marcaje")
    entrada = leer_habilidad("Entrada")
    fuerza = leer_habilidad("Fuerza")
    despeje = leer_habilidad("Despeje")
    return Defensa(nombre, dorsal, edad, marcaje, entrada, fuerza, despeje)


def registrar_medio():
    nombre, dorsal, edad = datos_basicos()
    pase_corto = leer_habilidad("Pase corto")
    pase_largo = leer_habilidad("Pase largo")
    vision = leer_habilidad("Vision")
    resistencia = leer_habilidad("Resistencia")
    return MedioCampo(nombre, dorsal, edad, pase_corto, pase_largo, vision, resistencia)


def registrar_delantero():
    nombre, dorsal, edad = datos_basicos() #Desempaquetado de tupla
    tiro = leer_habilidad("Tiro")
    regate = leer_habilidad("Regate")
    velocidad = leer_habilidad("Velocidad")
    definicion = leer_habilidad("Definicion")
    return Delantero(nombre, dorsal, edad, tiro, regate, velocidad, definicion)


def main():
    print("===== GESTION DE CONVOCATORIA - MUNDIAL 2026 =====")

    # El DT es el usuario del sistema
    nombre_dt = input("Nombre del DT: ")
    edad_dt = leer_edad("Edad del DT: ")
    seleccion = input("Seleccion que dirige: ")
    dt = DT(nombre_dt, edad_dt, seleccion)
    print(f"\nBienvenido, {dt.get_nombre()} (DT de {dt.get_seleccion()})")

    analisis = Analisis()

    while True:
        print("\n----- MENU -----")
        print("1. Registrar arquero")
        print("2. Registrar defensa")
        print("3. Registrar medio campo")
        print("4. Registrar delantero")
        print("5. Ver analisis de la convocatoria")
        print("6. Salir")
        opcion = leer_entero("Opcion: ")

        if opcion == 1:
            analisis.agregar_jugador(registrar_arquero())
            print("Arquero registrado")
        elif opcion == 2:
            analisis.agregar_jugador(registrar_defensa())
            print("Defensa registrado")
        elif opcion == 3:
            analisis.agregar_jugador(registrar_medio())
            print("Medio campo registrado")
        elif opcion == 4:
            analisis.agregar_jugador(registrar_delantero())
            print("Delantero registrado")
        elif opcion == 5:
            analisis.imprimir_convocatoria()
        elif opcion == 6:
            print(f"Hasta luego, DT {dt.get_nombre()}")
            break
        else:
            print("Opcion no valida")



main()