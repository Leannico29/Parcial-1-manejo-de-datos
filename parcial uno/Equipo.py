from jugador import Jugador
from Estadistica import Estadisticas
import json
import csv
import re

class Equipo:
    def __init__(self):
        self.jugadores = []

    def cargar_datos_desde_json(self, archivo):
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
                jugadores = [Jugador(Estadisticas(**jugador['estadisticas']), jugador['nombre'], jugador['posicion'], jugador['logros']) for jugador in datos['jugadores']]
                self.jugadores = jugadores
            print("Datos cargados exitosamente desde el archivo JSON.")
        except FileNotFoundError:
                print("Archivo no encontrado. Por favor, asegúrate de que el archivo JSON exista.")
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON. Por favor, verifica el formato del archivo.")
        except KeyError:
            print("Clave faltante en el archivo JSON. Por favor, verifica la estructura del archivo.")



    




