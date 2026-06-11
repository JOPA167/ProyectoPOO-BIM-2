
from jugador import Jugador

class Defensa(Jugador):
    def __init__(self, nombre, dorsal, edad, marcaje, entrada, fuerza, despeje):
        super().__init__(nombre, dorsal, edad)
        self.__marcaje = marcaje
        self.__entrada = entrada
        self.__fuerza = fuerza
        self.__despeje = despeje
        self._habilidades = [marcaje, entrada, fuerza, despeje]

    # Getters
    def get_marcaje(self):
        return self.__marcaje

    def get_entrada(self):
        return self.__entrada

    def get_fuerza(self):
        return self.__fuerza

    def get_despeje(self):
        return self.__despeje

    # Setters
    def set_marcaje(self, valor):
        self.__marcaje = valor
        self.__actualizar_habilidades()

    def set_entrada(self, valor):
        self.__entrada = valor
        self.__actualizar_habilidades()

    def set_fuerza(self, valor):
        self.__fuerza = valor
        self.__actualizar_habilidades()

    def set_despeje(self, valor):
        self.__despeje = valor
        self.__actualizar_habilidades()

    def __actualizar_habilidades(self):
        self._habilidades = [self.__marcaje, self.__entrada, self.__fuerza, self.__despeje]

    def get_posicion(self):
        return "Defensa"
