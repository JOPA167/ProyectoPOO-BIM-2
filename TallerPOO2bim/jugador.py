
# Incluye la funcion calcular_promedio() que reutilizan las clases hijas

from persona import *

class Jugador(Persona):
    def __init__(self, nombre, dorsal, edad):
        super().__init__(nombre, edad) #Atributos que le pertenecen a Persona
        self.__dorsal = dorsal           # atributo privado
        self._habilidades = []           # atributo protegido # arreglo de habilidaes

                                        # habilidades es protegido para que todos se les obtiene el promedio independientemente de
                                        # la posicion.

    def get_dorsal(self):
        return self.__dorsal

    def set_dorsal(self, dorsal):
        if 1 <= dorsal <= 99:
            self.__dorsal = dorsal
        else:
            print("Dorsal no valido (1-99)")

    # Funcion para calcular el promedio de las habilidades
    # Cada clase hija llena la lista _habilidades con sus atributos propios
    def calcular_promedio(self):
        if len(self._habilidades) == 0:
            return 0
        return sum(self._habilidades) / len(self._habilidades)

    def get_posicion(self):
        return "Sin posicion"

    def mostrar_info(self):
        return (f"#{self.__dorsal} {self.get_nombre()} | Edad: {self.get_edad()} | "
                f"Posicion: {self.get_posicion()} | Promedio: {self.calcular_promedio():.2f}")
