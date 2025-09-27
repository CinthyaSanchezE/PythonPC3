"""
EJERCICIO 2 del MÓDULO 3:
NOMBRE: CINTHYA ELIZABETH SANCHEZ ESPIRITU
"""
# TEMA: FUNCIONES
# Resolver estos problemas en un único script .py. Agregar control de errores según sea conveniente. Podría realizar un programa menú que permita realizar 
# todos los puntos mencionados.

# PROBLEMA2: Realizar una función que permita la carga de n alumnos. Por cada alumno se deberá preguntar el nombre completo y permitir el ingreso de 3 notas. 
# Las notas deben estar comprendidas entre 0 y 10. Devolver el listado de alumnos.

# PROBLEMA3: Definir una clase llamada “RECTANGULO” que puede ser construida por los atributos largo y ancho. La clase “RECTANGULO” debe tener un método 
# que puede calcular el área utilizando los atributos de la clase. Además cree una clase CUADRADO que heredé de rectangulo. Cree un objeto de tipo rectangulo 
# y 1 de tipo cuadrado.

# PROBLEMA4: Definir una función que dado un listado de alumnos evalúe cuántos aprobaron y cuántos desaprobaron, teniendo en cuenta que se aprueba con 4. 
# La nota será el promedio de las 3 notas para cada alumno.

# PROBLEMA5: Informar el promedio de nota del curso total.

# PROBLEMA6: Realizar una función que indique quién tuvo el promedio más alto y quién tuvo la nota promedio más baja.

# PROBLEMA7: Realizar una función que permita buscar un alumno por nombre, siendo el nombre completo o parcial, y devuelva una lista con los n alumnos 
# que concuerden con ese nombre junto con todos sus datos, incluido el promedio de sus notas.

class Rectangulo:
    def __init__(self, largo, ancho):
        if not isinstance(largo, (int, float)) or not isinstance(ancho, (int, float)) or largo <= 0 or ancho <= 0:
            raise ValueError("Largo y ancho deben ser números positivos.")
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

    def __str__(self): # Para una mejor representación al imprimir el objeto
        return f"Rectángulo (Largo: {self.largo}, Ancho: {self.ancho}, Área: {self.area()})"

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        if not isinstance(lado, (int, float)) or lado <= 0:
            raise ValueError("El lado debe ser un número positivo.")
        super().__init__(lado, lado) # Un cuadrado tiene el mismo largo y ancho

    def __str__(self): # Para una mejor representación al imprimir el objeto
        return f"Cuadrado (Lado: {self.largo}, Área: {self.area()})"

def cargar_alumnos():
    alumnos_nuevos = []
    print("\n--- Carga de Alumnos ---")
    while True:
        nombre = input("Ingrese el nombre completo del alumno (o 'salir' para terminar la carga): ")
        if nombre.lower() == 'salir':
            break
        
        notas = []
        for i in range(3):
            while True:
                try:
                    nota_str = input(f"Ingrese la nota {i+1} para {nombre} (entre 0 y 10): ")
                    nota = float(nota_str)
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Error: La nota debe estar entre 0 y 10. Intente de nuevo.")
                except ValueError:
                    print("Error: Entrada inválida. Por favor, ingrese un número para la nota.")
        alumnos_nuevos.append({'nombre': nombre, 'notas': notas})
    print(f"Se cargaron {len(alumnos_nuevos)} nuevos alumnos.")
    return alumnos_nuevos

def evaluar_alumnos(alumnos):
    if not alumnos:
        print("No hay alumnos cargados para evaluar.")
        return
    aprobados = 0
    desaprobados = 0
    print("\n--- Evaluación de Alumnos ---")
    for alumno in alumnos:
        if alumno['notas']: # Asegurarse de que haya notas para evitar ZeroDivisionError
            promedio = sum(alumno['notas']) / len(alumno['notas'])
            print(f"- {alumno['nombre']}: Promedio {promedio:.2f} - {'Aprobado' if promedio >= 4 else 'Desaprobado'}")
            if promedio >= 4:
                aprobados += 1
            else:
                desaprobados += 1
        else:
            print(f"- {alumno['nombre']}: Sin notas registradas.")
    print(f"\nResumen: {aprobados} alumnos aprobados, {desaprobados} alumnos desaprobados.")
    return aprobados, desaprobados

def promedio_curso(alumnos):
    if not alumnos:
        print("No hay alumnos cargados para calcular el promedio del curso.")
        return 0
    total_promedios = 0
    alumnos_con_notas = 0
    for alumno in alumnos:
        if alumno['notas']:
            total_promedios += sum(alumno['notas']) / len(alumno['notas'])
            alumnos_con_notas += 1
    
    if alumnos_con_notas > 0:
        promedio = total_promedios / alumnos_con_notas
        print(f"\n--- Promedio General del Curso ---")
        print(f"El promedio total del curso es: {promedio:.2f}")
        return promedio
    else:
        print("No hay alumnos con notas para calcular el promedio del curso.")
        return 0

def extremos_promedio(alumnos):
    if not alumnos:
        print("No hay alumnos cargados para encontrar promedios extremos.")
        return None, None
    
    promedios_validos = []
    for alumno in alumnos:
        if alumno['notas']:
            promedios_validos.append((alumno['nombre'], sum(alumno['notas']) / len(alumno['notas'])))
            
    if not promedios_validos:
        print("No hay alumnos con notas válidas para calcular promedios extremos.")
        return None, None

    max_promedio = max(promedios_validos, key=lambda x: x[1])
    min_promedio = min(promedios_validos, key=lambda x: x[1])
    
    print("\n--- Promedios Más Altos y Más Bajos ---")
    print(f"Alumno con el promedio más alto: {max_promedio[0]} con {max_promedio[1]:.2f}")
    print(f"Alumno con el promedio más bajo: {min_promedio[0]} con {min_promedio[1]:.2f}")
    return max_promedio, min_promedio

def buscar_alumno(alumnos):
    if not alumnos:
        print("No hay alumnos cargados para buscar.")
        return
    nombre_buscar = input("Ingrese el nombre completo o parcial del alumno a buscar: ")
    resultados = []
    for alumno in alumnos:
        if nombre_buscar.lower() in alumno['nombre'].lower():
            if alumno['notas']:
                promedio = sum(alumno['notas']) / len(alumno['notas'])
            else:
                promedio = "N/A (sin notas)"
            alumno_info = alumno.copy() # Copia para no modificar el original
            alumno_info['promedio'] = promedio
            resultados.append(alumno_info)
    
    print(f"\n--- Resultados de Búsqueda para '{nombre_buscar}' ---")
    if resultados:
        for alumno_encontrado in resultados:
            print(f"  - Nombre: {alumno_encontrado['nombre']}, Notas: {alumno_encontrado['notas']}, Promedio: {alumno_encontrado['promedio']}")
    else:
        print("No se encontraron alumnos con ese nombre o parte del nombre.")
    return resultados

def demostrar_formas():
    print("\n--- Demostración de Rectángulo y Cuadrado ---")
    try:
        largo_str = input("Ingrese el largo para el Rectángulo: ")
        largo = float(largo_str)
        ancho_str = input("Ingrese el ancho para el Rectángulo: ")
        ancho = float(ancho_str)
        rectangulo = Rectangulo(largo, ancho)
        print(f"Rectángulo creado: {rectangulo}")

        lado_str = input("Ingrese el lado para el Cuadrado: ")
        lado = float(lado_str)
        cuadrado = Cuadrado(lado)
        print(f"Cuadrado creado: {cuadrado}")

    except ValueError as e:
        print(f"Error al crear la forma: {e}. Asegúrese de ingresar números positivos.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def main_menu():
    alumnos_cargados = [] # Esta lista persistirá mientras el menú esté activo

    while True:
        print("\n" + "="*40)
        print("          MENÚ PRINCIPAL")
        print("="*40)
        print("1. Cargar nuevos alumnos")
        print("2. Evaluar alumnos (Aprobados/Desaprobados)")
        print("3. Calcular promedio general del curso")
        print("4. Identificar promedio más alto y más bajo")
        print("5. Buscar alumno por nombre")
        print("6. Demostrar Clases Rectángulo y Cuadrado")
        print("7. Mostrar listado de alumnos actuales")
        print("0. Salir")
        print("="*40)

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nuevos = cargar_alumnos()
            alumnos_cargados.extend(nuevos) # Agrega los nuevos alumnos a la lista existente
        elif opcion == '2':
            evaluar_alumnos(alumnos_cargados)
        elif opcion == '3':
            promedio_curso(alumnos_cargados)
        elif opcion == '4':
            extremos_promedio(alumnos_cargados)
        elif opcion == '5':
            buscar_alumno(alumnos_cargados)
        elif opcion == '6':
            demostrar_formas()
        elif opcion == '7':
            if alumnos_cargados:
                print("\n--- Listado de Alumnos Actuales ---")
                for alum in alumnos_cargados:
                    print(f"Nombre: {alum['nombre']}, Notas: {alum['notas']}")
            else:
                print("No hay alumnos cargados.")
        elif opcion == '0':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 0 al 7.")

if __name__ == "__main__":
    main_menu()

