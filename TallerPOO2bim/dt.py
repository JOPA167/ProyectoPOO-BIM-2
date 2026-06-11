
from persona import Persona

class DT(Persona):
    def __init__(self, nombre, edad, seleccion):
        super().__init__(nombre, edad)   # llama al constructor de Persona
        self.__seleccion = seleccion     # atributo privado propio del DT

    def get_seleccion(self):
        return self.__seleccion

    def set_seleccion(self, seleccion):
        self.__seleccion = seleccion

    def mostrar_info(self):
        return f"DT: {self.get_nombre()} | Edad: {self.get_edad()} | Seleccion: {self.__seleccion}"
