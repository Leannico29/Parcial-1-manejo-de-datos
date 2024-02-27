from Estadistica import Estadisticas

class Jugador:

    def __init__(self, estadisticas:Estadisticas, nombre: str, posicion: str, logros: list[str]):
        self.__estadisticas = estadisticas
        self._nombre = nombre
        self.__posicion = posicion
        self.__logros = logros

    @property
    def nombre(self): 
        return self._nombre

    @nombre.setter
    def nombre(self, nombre:str):
        self._nombre = nombre 

    @property
    def estadistica(self):
        return self.__estadísticas 

    @estadistica.setter
    def estadistica(self, estadistica:Estadisticas):
        self.__estadísticas = estadistica 

    @property
    def posicion(self):
        return self.__posicion 

    @posicion.setter
    def posicion(self, posicion:str):
        self.__posicion = posicion 

    @property
    def logros(self):
        return self.__logros 

    @logros.setter
    def logros(self, logros:list[str]):
        self.__logros = logros 
        
    def obtener_estadisticas(self):
        return self.__estadisticas