"""
EJERCICIO 8 del MÓDULO 3:
NOMBRE: CINTHYA ELIZABETH SANCHEZ ESPIRITU
"""
# TEMA: LIBRERIAS

#PROBLEMA8: Empleando la API de SUNAT vista en clase, debemos obtener los diferentes valores para el tipo de cambio 
# durante el año 2025 hasta donde se tenga información. Una vez realizado ello calcular: 
# Obtener las fechas donde el valor de compra del dólar sea el mínimo. 
# Obtener las fechas donde el valor de venta del dólar sea máximo.
# Obtener aquellas fechas donde el valor de la diferencia de compraventa sea máxima. 
# EJEMPLO API: https://api.apis.net.pe/v1/tipo-cambio-sunat?month=5&year=2025 
# DOCUMENTACIÓN API: https://apis.net.pe/api-tipo-cambio.html 
# Para el manejo de excepciones se puede realizar lo siguiente: import requests, try, except requests.RequestException

import requests
import json
# La librería datetime ayuda a trabajar con fechas, aquí solo se usa de referencia.
from datetime import date

# --- 1. CONFIGURACIÓN DEL SCRIPT ---
BASE_URL = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
ANIO = 2025 # El año solicitado para la consulta

# Consulta de un año futuro (2025), asumimos que el bucle debe ir hasta el último mes, o hasta que la API deje de dar información.
MES_INICIO = 1
MES_FIN = 12 # Iremos de Enero (1) a Diciembre (12)

# Lista vacía donde se guardará todos los tipos de cambio de todo el año
datos_tipo_cambio = []

print(f"--- INICIO DE CONSULTA: Año {ANIO} ---")

# --- 2. RECORRER Y CONSULTAR LA API MES A MES ---
for mes in range(MES_INICIO, MES_FIN + 1):
    # Crear la URL completa para el mes actual
    url_consulta = f"{BASE_URL}?month={mes}&year={ANIO}"

    print(f"Consultando datos para el mes: {mes}")

    try:
        # Petición a la API usando requests
        response = requests.get(url_consulta, timeout=10)
        # Revisa si hubo un error HTTP (como 404 o 500)
        response.raise_for_status()

        # Convertir la respuesta de texto a un formato que Python, se entiende (JSON/Diccionario)
        data_mes = response.json()

        # La API retorna una lista de días. Se revisa si tiene datos.
        if isinstance(data_mes, list) and data_mes:
            # Si hay datos, los agregamos a nuestra lista principal
            datos_tipo_cambio.extend(data_mes)
        elif not data_mes:
            # Si la lista está vacía, probablemente es un mes sin información (aún no existe)
            print(f"ADVERTENCIA: No hay datos disponibles para el mes {mes}. Finalizando la búsqueda.")
            break # Detenemos el bucle porque no habrá más información

    # --- Manejo de Errores (Excepciones) ---
    except requests.exceptions.RequestException as e:
        # Captura errores de conexión, DNS, o errores HTTP.
        print(f"ERROR: Falló la conexión o la petición para el mes {mes}. Mensaje: {e}")
        break # Detenemos el script si hay un error de red
    except json.JSONDecodeError:
        # Captura si la respuesta no es un JSON válido.
        print(f"ERROR: La respuesta del servidor para el mes {mes} no es un JSON válido.")
        break
    except Exception as e:
        # Captura cualquier otro error inesperado.
        print(f"ERROR: Ocurrió un error inesperado en el mes {mes}. Mensaje: {e}")
        break

print(f"--- CONSULTA FINALIZADA. Registros obtenidos: {len(datos_tipo_cambio)} ---")

# --- 3. ANÁLISIS DE LOS DATOS RECOLECTADOS ---

# Inicializar variables para encontrar los valores extremos.
# Se usa 'inf' (infinito) para asegurar que el primer dato lo reemplace.
min_compra = float('inf')
max_venta = float('-inf')
max_diferencia = float('-inf')

# Listas para guardar las fechas que cumplen la condición (puede ser más de una)
fechas_min_compra = []
fechas_max_venta = []
fechas_max_diferencia = []


# Recorrer todos los datos de tipo de cambio obtenidos
for registro in datos_tipo_cambio:
    try:
        fecha = registro['fecha']
        # Convertir los valores de texto (string) a números decimales (float)
        compra = float(registro['compra'])
        venta = float(registro['venta'])
        diferencia = venta - compra

    except (ValueError, TypeError, KeyError):
        # Si un dato no existe o no es un número, saltamos ese registro.
        print(f"Aviso: Se omitió un registro inválido o incompleto en la fecha: {registro.get('fecha', 'Desconocida')}")
        continue # 'continue' hace que el bucle pase al siguiente registro

    # a. Obtener las fechas donde el valor de compra del dólar sea el mínimo.
    if compra < min_compra:
        min_compra = compra
        fechas_min_compra = [fecha] # Nuevo mínimo: reiniciamos la lista
    elif compra == min_compra:
        fechas_min_compra.append(fecha) # Mismo mínimo: agregamos la fecha

    # b. Obtener las fechas donde el valor de venta del dólar sea máximo.
    if venta > max_venta:
        max_venta = venta
        fechas_max_venta = [fecha] # Nuevo máximo: reiniciamos la lista
    elif venta == max_venta:
        fechas_max_venta.append(fecha) # Mismo máximo: agregamos la fecha

    # c. Obtener aquellas fechas donde el valor de la diferencia de compraventa sea máxima.
    if diferencia > max_diferencia:
        max_diferencia = diferencia
        fechas_max_diferencia = [fecha] # Nuevo máximo: reiniciamos la lista
    elif diferencia == max_diferencia:
        fechas_max_diferencia.append(fecha) # Mismo máximo: agregamos la fecha

# --- 4. IMPRIMIR RESULTADOS FINALES ---

print("\n" + "=" * 50)
print("             RESULTADOS DEL ANÁLISIS DE TIPO DE CAMBIO")
print("=" * 50)

# 1. Compra Mínima
print("\n--- 1. Fechas con el MÍNIMO Valor de Compra ---")
print(f"Valor Mínimo de Compra: {min_compra:.3f}")
# Usamos set() para quitar fechas duplicadas, aunque en este caso es poco probable
for f in sorted(list(set(fechas_min_compra))):
    print(f"  > Fecha: {f}")

# 2. Venta Máxima
print("\n--- 2. Fechas con el MÁXIMO Valor de Venta ---")
print(f"Valor Máximo de Venta: {max_venta:.3f}")
for f in sorted(list(set(fechas_max_venta))):
    print(f"  > Fecha: {f}")

# 3. Diferencia Máxima
print("\n--- 3. Fechas con la MÁXIMA Diferencia (Venta - Compra) ---")
print(f"Máxima Diferencia (Venta - Compra): {max_diferencia:.4f}")
for f in sorted(list(set(fechas_max_diferencia))):
    print(f"  > Fecha: {f}")

print("\n" + "=" * 50)

