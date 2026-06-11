
from jugador import Jugador

class MedioCampo(Jugador):
    def __init__(self, nombre, dorsal, edad, pase_corto, pase_largo, vision, resistencia):
        super().__init__(nombre, dorsal, edad)
        self.__pase_corto = pase_corto
        self.__pase_largo = pase_largo
        self.__vision = vision
        self.__resistencia = resistencia
        self._habilidades = [pase_corto, pase_largo, vision, resistencia]

    # Getters
    def get_pase_corto(self):
        return self.__pase_corto

    def get_pase_largo(self):
        return self.__pase_largo

    def get_vision(self):
        return self.__vision

    def get_resistencia(self):
        return self.__resistencia

    # Setters
    def set_pase_corto(self, valor):
        self.__pase_corto = valor
        self.__actualizar_habilidades()

    def set_pase_largo(self, valor):
        self.__pase_largo = valor
        self.__actualizar_habilidades()

    def set_vision(self, valor):
        self.__vision = valor
        self.__actualizar_habilidades()

    def set_resistencia(self, valor):
        self.__resistencia = valor
        self.__actualizar_habilidades()

    def __actualizar_habilidades(self):
        self._habilidades = [self.__pase_corto, self.__pase_largo, self.__vision, self.__resistencia]

    def get_posicion(self):
        return "Medio Campo"
