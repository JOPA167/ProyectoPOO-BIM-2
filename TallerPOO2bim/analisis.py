

from arquero import Arquero
from defensa import Defensa
from medio_campo import MedioCampo
from delantero import Delantero

class Analisis:
    def __init__(self):
        # 4 listas, una por posicion
        self.__arqueros = []
        self.__defensas = []
        self.__medios = []
        self.__delanteros = []

    # Agrega el jugador a la lista de su posicion segun su tipo
    #Usamo isinstane para ver si el objeto pertenece a una clase

    def agregar_jugador(self, jugador):
        if isinstance(jugador, Arquero):
            self.__arqueros.append(jugador)
        elif isinstance(jugador, Defensa):
            self.__defensas.append(jugador)
        elif isinstance(jugador, MedioCampo):
            self.__medios.append(jugador)
        elif isinstance(jugador, Delantero):
            self.__delanteros.append(jugador)
        else:
            print("Tipo de jugador no reconocido")

    # Devuelve un arreglo con los promedios de habilidades de una lista
    def obtener_promedios(self, lista):
        promedios = []
        for jugador in lista:
            promedios.append(jugador.calcular_promedio())
        return promedios

    # Bubble sort: ordena la lista de jugadores de mayor a menor promedio
    def bubble_sort(self, lista):
        n = len(lista)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if lista[j].calcular_promedio() < lista[j + 1].calcular_promedio():
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista

    # Imprime una lista ordenada de mas a menos habilidoso
    def imprimir_lista(self, lista, titulo):
        print(f"\n--- {titulo} (de mas a menos habilidoso) ---")
        if len(lista) == 0:
            print("Sin jugadores registrados")
            return
        self.bubble_sort(lista)
        for jugador in lista:
            print(jugador.mostrar_info())

    def imprimir_arqueros(self):
        self.imprimir_lista(self.__arqueros, "ARQUEROS")

    def imprimir_defensas(self):
        self.imprimir_lista(self.__defensas, "DEFENSAS")

    def imprimir_medios(self):
        self.imprimir_lista(self.__medios, "MEDIO CAMPO")

    def imprimir_delanteros(self):
        self.imprimir_lista(self.__delanteros, "DELANTEROS")

    # Imprime toda la convocatoria ordenada por posicion
    def imprimir_convocatoria(self):
        print("\n========== ANALISIS DE LA CONVOCATORIA ==========")
        self.imprimir_arqueros()
        self.imprimir_defensas()
        self.imprimir_medios()
        self.imprimir_delanteros()
