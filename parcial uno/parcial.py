import csv
from Equipo import *

equipo = Equipo()
equipo.cargar_datos_desde_json('dream_team.json')


def quick_sort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0][1]
        menores = [(nombre, puntos) for nombre, puntos in list if puntos < pivot]
        iguales = [(nombre, puntos) for nombre, puntos in list if puntos == pivot]
        mayores = [(nombre, puntos) for nombre, puntos in list if puntos > pivot]
        return quick_sort(menores) + iguales + quick_sort(mayores)

def mostrar_jugadores(equipo):
    ''' Mostrar la lista de todos los jugadores del Dream Team. Con el formato: Nombre Jugador - Posición. '''
    for i, jugador in enumerate(equipo.jugadores):
        nombre = jugador.nombre 
        posicion = jugador.posicion
        print(f'{nombre} - {posicion}')

def mostrar_estadisticas_jugador(equipo):
    # Pide al usuario que seleccione un jugador por su índice
    indice_jugador = input("Por favor, selecciona un jugador por su índice: ")

    # Valida la entrada con regex
    if re.match(r'^\d+$', indice_jugador):
        indice_jugador = int(indice_jugador) - 1 # Ajusta para el índice basado en cero
        if 0 <= indice_jugador < len(equipo.jugadores):
            # Llama al método en el jugador seleccionado
            jugador = equipo.jugadores[indice_jugador]
            estadisticas = jugador.obtener_estadisticas()
            print(f"Temporadas jugadas: {estadisticas.temporadas}")
            print(f"Puntos totales: {estadisticas.puntos_totales}")
            print(f"Rebotes totales: {estadisticas.rebotes_totales}")
            print(f"Asistencias totales: {estadisticas.asistencias_totales}")
            print(f"Robos totales: {estadisticas.robos_totales}")
            print(f"Bloqueos totales: {estadisticas.bloqueos_totales}")
            print(f"Porcentaje de tiros de campo: {estadisticas.porcentaje_tiros_de_campo}")
            print(f"Porcentaje de tiros libres: {estadisticas.porcentaje_tiros_libres}")
            print(f"Porcentaje de tiros triples: {estadisticas.porcentaje_tiros_triples}")

            respuesta = input("¿Deseas guardar las estadísticas en un archivo CSV? (s/n): ")

            if respuesta.lower() == 's':
                try:
                    nombre_archivo = input("Por favor, introduce el nombre del archivo CSV: ") 
                    with open(nombre_archivo + ".csv", "w") as archivo: 
                        archivo.write('Estadistica | Valor\n')
                        archivo.write('Temporadas jugadas,' + str(estadisticas.temporadas) + '\n')
                        archivo.write('Puntos totales,' + str(estadisticas.puntos_totales) + '\n')
                        archivo.write('Rebotes totales,' + str(estadisticas.rebotes_totales) + '\n')
                        archivo.write('Asistencias totales,' + str(estadisticas.asistencias_totales) + '\n')
                        archivo.write('Robos totales,' + str(estadisticas.robos_totales) + '\n')
                        archivo.write('Bloqueos totales,' + str(estadisticas.bloqueos_totales) + '\n')
                        archivo.write('Porcentaje de tiros de campo,' + str(estadisticas.porcentaje_tiros_de_campo) + '\n')
                        archivo.write('Porcentaje de tiros libres,' + str(estadisticas.porcentaje_tiros_libres) + '\n')
                        archivo.write('Porcentaje de tiros triples,' + str(estadisticas.porcentaje_tiros_triples) + '\n')
                    print('Archivo creado!')
                except Exception as a:
                    print('Ocurrio un error y el archivo no se pudo crear')
                    print(f'ERROR: {a}')
                    
            respuesta = input("¿Deseas guardar las estadísticas en un archivo json? (s/n): ")

            if respuesta.lower() == 's':
                try:
                    nombre_archivo = input("Por favor, introduce el nombre del archivo JSON: ")
                    datos = {
                        "Temporadas jugadas": estadisticas.temporadas,
                        "Puntos totales": estadisticas.puntos_totales,
                        "Rebotes totales": estadisticas.rebotes_totales,
                        "Asistencias totales": estadisticas.asistencias_totales,
                        "Robos totales": estadisticas.robos_totales,
                        "Bloqueos totales": estadisticas.bloqueos_totales,
                        "Porcentaje de tiros de campo": estadisticas.porcentaje_tiros_de_campo,
                        "Porcentaje de tiros libres": estadisticas.porcentaje_tiros_libres,
                        "Porcentaje de tiros triples": estadisticas.porcentaje_tiros_triples
                    }

                    with open(nombre_archivo + ".json", "w") as archivo:
                        json.dump(datos, archivo, indent=4)
                    print('Archivo creado!')
                except Exception as e:
                    print(f'Ocurrió un error y el archivo no se pudo crear: {e}')

def buscar_por_nombre(equipo):
    '''Permitir al usuario buscar un jugador por su nombre (validar con regex) y mostrar sus logros'''
    patron = str(input('Ingrese el nombre: '))
    for jugador in equipo.jugadores:
        hay_match = re.search(patron, jugador.nombre, re.IGNORECASE)
        if hay_match:
            logros = jugador.logros
            logros_corregidos = [logro.encode('latin-1').decode('utf-8') for logro in logros]
            print(logros_corregidos)

def calcular_promedio_puntos(equipo):
    '''Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente.'''

    jugadores_promedios = []
    for jugador in equipo.jugadores:
        estadisticas = jugador.obtener_estadisticas()
        promedio_puntos = estadisticas.puntos_totales / estadisticas.temporadas
        jugadores_promedios.append((jugador.nombre, promedio_puntos))

    # Ordenar los jugadores por el promedio de puntos por partido de manera ascendente
    jugadores_ordenados = quick_sort(jugadores_promedios)

    # Mostrar los jugadores y sus promedios
    for nombre, promedio in jugadores_ordenados:
        print(f'El promedio de puntos por partido de {nombre} es: {promedio}')

def buscar_por_nombre_salon_fama(equipo):
    patron = str(input('Ingrese el nombre: '))
    for jugador in equipo.jugadores:
        hay_match = re.search(patron, jugador.nombre, re.IGNORECASE)
        if hay_match:
            logros = jugador.logros
            logros_corregidos = [logro.encode('latin-1').decode('utf-8') for logro in logros]
            if 'Miembro del Salon de la Fama del Baloncesto' in logros_corregidos:
                print(f'{jugador.nombre} es miembro del Salón de la Fama del Baloncesto.')
            else:
                print(f'{jugador.nombre} no es miembro del Salón de la Fama del Baloncesto.')

def mostrar_jugador_mayor_rebotes(equipo):
    '''Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.'''
    # Inicializa la lista de jugadores con la mayor cantidad de rebotes totales
    jugadores_mayores_rebotes = []
    max_rebotes_totales = 0

    # Itera sobre los jugadores y encuentra el jugador con la mayor cantidad de rebotes totales
    for jugador in equipo.jugadores:
        estadisticas = jugador.obtener_estadisticas()
        if estadisticas.rebotes_totales > max_rebotes_totales:
            jugadores_mayores_rebotes = [jugador]
            max_rebotes_totales = estadisticas.rebotes_totales
        elif estadisticas.rebotes_totales == max_rebotes_totales:
            jugadores_mayores_rebotes.append(jugador)

    # Muestra al jugador con la mayor cantidad de rebotes totales
    if jugadores_mayores_rebotes:
        for jugador in jugadores_mayores_rebotes:
            print(f'El jugador {jugador.nombre} tiene la mayor cantidad de rebotes totales con {max_rebotes_totales} rebotes totales.')

def listado_rebotes_descendente(equipo):
    '''3- "rebotes_totales" Ordenar el listado de manera descendente(el mayor arriba) y mostrar el listado'''
    jugadores_rebotes = []
    for jugador in equipo.jugadores:
        estadisticas = jugador.obtener_estadisticas()
        jugadores_rebotes.append((jugador.nombre, estadisticas.rebotes_totales))

    # Ordenar los jugadores por el promedio de puntos por partido de manera ascendente
    lista_rebotes_ordenada = quick_sort(jugadores_rebotes)

    # Mostrar los jugadores y sus rebotes
    for nombre, rebotes in lista_rebotes_ordenada[::-1]:
        print(f"{nombre}: {rebotes}")

    respuesta = input("¿Deseas guardar la lista en un archivo CSV? (s/n): ")
    
    if respuesta.lower() == 's':
        nombre_archivo = input("Por favor, introduce el nombre del archivo CSV: ")
    

        with open(nombre_archivo + '.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for nombre, rebotes in lista_rebotes_ordenada[::-1]:
                writer.write(f'{nombre},{rebotes}')

def suma_robos_bloqueos(equipo):
    jugadores_suma = []
    acumulador_suma = 0
    for jugador in equipo.jugadores:
        estadisticas = jugador.obtener_estadisticas()
        robos = estadisticas.robos_totales
        bloqueos = estadisticas.bloqueos_totales
        suma = robos + bloqueos
        jugadores_suma.append((jugador.nombre, suma))
        acumulador_suma += suma

    lista_jugadores_suma_ordenada = quick_sort(jugadores_suma)
    
    for jugador in equipo.jugadores:
        patron = jugador.nombre
        hay_match = any(patron in nombre for nombre, _ in lista_jugadores_suma_ordenada)
        estadisticas = jugador.obtener_estadisticas()
        robos = estadisticas.robos_totales
        bloqueos = estadisticas.bloqueos_totales
        if hay_match:

            for nombre, suma in lista_jugadores_suma_ordenada[::-1]:
                if patron == nombre:
                    porcentaje = (suma / acumulador_suma) * 100
                    print(f"Jugador: {nombre} | Robos: {robos} | Bloqueos: {bloqueos} | Suma de ambos: {suma} | ({(porcentaje):.3f}%)")

def filtro_cantidad_a_mostrar(equipo):
    cantidad = input('Indique la cantidad de jugadores que desea que se muestren:')
    cantidad = int(cantidad)
    while cantidad > 12:
        print('Error el numero debe ser menor que 12')
        cantidad = input('Indique la cantidad de jugadores que desea que se muestren:')
        cantidad = int(cantidad)
    
    jugadores_suma = []
    acumulador_suma = 0
    contador = 0
    for jugador in equipo.jugadores:
        estadisticas = jugador.obtener_estadisticas()
        robos = estadisticas.robos_totales
        bloqueos = estadisticas.bloqueos_totales
        suma = robos + bloqueos
        jugadores_suma.append((jugador.nombre, suma))
        acumulador_suma += suma

    lista_jugadores_suma_ordenada = quick_sort(jugadores_suma)
    
    for jugador in equipo.jugadores:
        if contador == cantidad:
            break
        patron = jugador.nombre
        hay_match = any(patron in nombre for nombre, _ in lista_jugadores_suma_ordenada)
        estadisticas = jugador.obtener_estadisticas()
        robos = estadisticas.robos_totales
        bloqueos = estadisticas.bloqueos_totales
        if hay_match:
            for nombre, suma in lista_jugadores_suma_ordenada[::-1]:
                if patron == nombre:
                    porcentaje = (suma / acumulador_suma) * 100
                    print(f"Jugador: {nombre} | Robos: {robos} | Bloqueos: {bloqueos} | Suma de ambos: {suma} | ({(porcentaje):.3f}%)")
                    contador += 1

def sqlite_posiciones(equipo):
    lista_de_posiciones = []
    for jugador in equipo.jugadores:
        posicion = jugador.posicion 
        if posicion not in lista_de_posiciones:
            lista_de_posiciones.append(posicion)

    texto = "Posiciones:"
    for valor in lista_de_posiciones:
        texto += f'\n{valor}'
        

    try:
        nombre_archivo = input("Nombre del archivo:") 
        with open(nombre_archivo + ".csv", "w") as archivo: 
            archivo.write(texto)
        print('Archivo creado!')
    except Exception:
        print('Ocurrio un error y el archivo no se pudo crear')
        print({Exception})

