"""
EJERCICIO 10 del MÓDULO 3:
NOMBRE: CINTHYA ELIZABETH SANCHEZ ESPIRITU
"""
# TEMA: LIBRERIAS

#PROBLEMA10: Del siguiente URL https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D 
# Descargue la imagen que más le agrade, según lo revisado en la clase. Posteriormente crear un programa que permita el 
# almacenamiento de la imagen como un archivo zip. Finalmente cree un código que permita hacer un unzip al archivo zipeado. 

import requests # Para descargar la imagen de la URL
import zipfile  # Para crear y abrir archivos ZIP
import io       # Para manejar datos binarios en memoria (opcional, pero buena práctica)

# --- 1. CONFIGURACIÓN ---
# URL de ejemplo de la imagen que usaremos (una foto de un perrito)
URL_IMAGEN = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
NOMBRE_IMAGEN = "imagen_favorita_de_Cinthya.jpg"
NOMBRE_ZIP = "imagen_comprimida_Cinthya.zip"
NOMBRE_EXTRAIDO = "imagen_extraida_Cinthya.jpg"

print("--- TAREA 1: DESCARGA DE IMAGEN ---")

# --- PARTE 1: DESCARGAR LA IMAGEN ---

try:
    # 1. Realizar la petición HTTP para obtener el contenido de la imagen
    print(f"Descargando imagen desde: {URL_IMAGEN[:50]}...")
    respuesta = requests.get(URL_IMAGEN, stream=True)
    respuesta.raise_for_status() # Lanza un error si la descarga falla (código 4xx o 5xx)

    # 2. Guardar el contenido binario de la imagen en un archivo local
    with open(NOMBRE_IMAGEN, 'wb') as archivo:
        # Usamos el contenido binario (respuesta.content) y lo escribimos ('wb' = write binary)
        archivo.write(respuesta.content)

    print(f"Imagen descargada y guardada como: {NOMBRE_IMAGEN}")

except requests.exceptions.RequestException as e:
    print(f"ERROR al descargar la imagen: {e}")
    exit() # Detenemos el programa si no se puede descargar

print("\n" + "-" * 30)
print("--- TAREA 2: COMPRIMIR LA IMAGEN EN UN ARCHIVO ZIP ---")

# --- PARTE 2: COMPRIMIR LA IMAGEN ---

try:
    # 1. Abrir o crear el archivo ZIP en modo escritura ('w')
    with zipfile.ZipFile(NOMBRE_ZIP, 'w', zipfile.ZIP_DEFLATED) as archivo_zip:
        # 2. Agregar la imagen al archivo ZIP
        # 'zipfile.ZIP_DEFLATED' indica que comprima el archivo
        archivo_zip.write(NOMBRE_IMAGEN, NOMBRE_IMAGEN)

    print(f"Imagen '{NOMBRE_IMAGEN}' ha sido comprimida en: {NOMBRE_ZIP}")

except FileNotFoundError:
    print(f"ERROR: No se encontró el archivo '{NOMBRE_IMAGEN}' para comprimir.")
except Exception as e:
    print(f"ERROR al crear el archivo ZIP: {e}")

print("\n" + "-" * 30)
print("--- TAREA 3: DESCOMPRIMIR EL ARCHIVO ZIP ---")

# --- PARTE 3: DESCOMPRIMIR EL ARCHIVO ZIP ---

try:
    # 1. Abrir el archivo ZIP en modo lectura ('r')
    with zipfile.ZipFile(NOMBRE_ZIP, 'r') as archivo_zip:
        # 2. Extraer el contenido. Indicamos el nombre del archivo dentro del zip
        # y le damos un nuevo nombre al archivo extraído.
        archivo_zip.extract(NOMBRE_IMAGEN, path='.', )

    # El archivo extraído tendrá el mismo nombre que tenía dentro del zip.
    # Si queremos darle otro nombre para verificar que se extrajo correctamente:
    import os
    os.rename(NOMBRE_IMAGEN, NOMBRE_EXTRAIDO)

    print(f"Archivo ZIP descomprimido.")
    print(f"El contenido ha sido extraído como: {NOMBRE_EXTRAIDO}")

except FileNotFoundError:
    print(f"ERROR: No se encontró el archivo ZIP: {NOMBRE_ZIP}")
except Exception as e:
    print(f"ERROR al descomprimir el archivo ZIP: {e}")

print("\n--- PROGRAMA FINALIZADO ---")
