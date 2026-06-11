

from jugador import Jugador

class Arquero(Jugador):
    def __init__(self, nombre, dorsal, edad, reflejos, posicionamiento, manejo_balon):
        super().__init__(nombre, dorsal, edad)
        self.__reflejos = reflejos
        self.__posicionamiento = posicionamiento
        self.__manejo_balon = manejo_balon
        # Se llena la lista protegida para reutilizar calcular_promedio()
        self._habilidades = [reflejos, posicionamiento, manejo_balon]

    # Getters
    def get_reflejos(self):
        return self.__reflejos

    def get_posicionamiento(self):
        return self.__posicionamiento

    def get_manejo_balon(self):
        return self.__manejo_balon

    # Setters
    def set_reflejos(self, valor):
        self.__reflejos = valor
        self.__actualizar_habilidades()

    def set_posicionamiento(self, valor):
        self.__posicionamiento = valor
        self.__actualizar_habilidades()

    def set_manejo_balon(self, valor):
        self.__manejo_balon = valor
        self.__actualizar_habilidades()

    def __actualizar_habilidades(self):
        self._habilidades = [self.__reflejos, self.__posicionamiento, self.__manejo_balon]

    def get_posicion(self):
        return "Arquero"
