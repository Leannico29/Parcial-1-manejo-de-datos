from parcial import *
import os

def menu(equipo):

    while True:
        opcion = input(
            '''
1) Mostrar lista de jugadores
2) Mostrar estadísticas de un jugador
3) Buscar jugador por nombre
4) Calcular el promedio de epuntos
5) Buscar si el jugador se encuentra en el salon de la fama
6) Jugador con mayor numero de rebotes
7) Mostrar el listado de rebotes en forma ascendente 
8) Informacion sobre robos y bloqueos
9) Informacion sobre robos y bloqueos con limite
10) CSV posiciones
11) Limpiar la consola
12) Salir
Seleccione una opción: '''
            
        )

        match opcion:
            case '1':
                mostrar_jugadores(equipo)
            case '2':
                mostrar_estadisticas_jugador(equipo)
            case '3':
                buscar_por_nombre(equipo)
            case '4':
                calcular_promedio_puntos(equipo)
            case '5':
                buscar_por_nombre_salon_fama(equipo)
            case '6':
                mostrar_jugador_mayor_rebotes(equipo)
            case '7':
                listado_rebotes_descendente(equipo)
            case '8':
                suma_robos_bloqueos(equipo)
            case '9':
                filtro_cantidad_a_mostrar(equipo)
            case '10':
                sqlite_posiciones(equipo)
            case '11':
                clear()
            case '12':
                print('Vuelva prontos')
                break


def clear():
    # Limpia la consola
    os.system('cls' if os.name == 'nt' else 'clear')

equipo = Equipo()
equipo.cargar_datos_desde_json('dream_team.json')
menu(equipo)