
from jugador import Jugador

class Delantero(Jugador):
    def __init__(self, nombre, dorsal, edad, tiro, regate, velocidad, definicion):
        super().__init__(nombre, dorsal, edad)
        self.__tiro = tiro
        self.__regate = regate
        self.__velocidad = velocidad
        self.__definicion = definicion
        self._habilidades = [tiro, regate, velocidad, definicion]

    # Getters
    def get_tiro(self):
        return self.__tiro

    def get_regate(self):
        return self.__regate

    def get_velocidad(self):
        return self.__velocidad

    def get_definicion(self):
        return self.__definicion

    # Setters
    def set_tiro(self, valor):
        self.__tiro = valor
        self.__actualizar_habilidades()

    def set_regate(self, valor):
        self.__regate = valor
        self.__actualizar_habilidades()

    def set_velocidad(self, valor):
        self.__velocidad = valor
        self.__actualizar_habilidades()

    def set_definicion(self, valor):
        self.__definicion = valor
        self.__actualizar_habilidades()

    def __actualizar_habilidades(self):
        self._habilidades = [self.__tiro, self.__regate,
                             self.__velocidad, self.__definicion]

    def get_posicion(self):
        return "Delantero"
