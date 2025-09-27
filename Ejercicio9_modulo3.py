"""
EJERCICIO 9 del MÓDULO 3:
NOMBRE: CINTHYA ELIZABETH SANCHEZ ESPIRITU
"""
# TEMA: LIBRERIAS

#PROBLEMA9: FIGlet, llamado así por las cartas de Frank, Ian y Glen, es un programa de principios de la década de 1990 para 
# hacer letras grandes a partir de texto ordinario, una forma de arte ASCII: 
# - En la siguiente web puede ver una lista de fuentes admitidas por FIGlet figlet.org/examples.html 
# - Desde entonces, FIGlet ha sido portado a Python como un módulo llamado pyfiglet. 
# Cree un programa el cual cumpla con las siguientes especificaciones: 
# - Solicite al usuario el nombre de una fuente a utilizar. En caso no sé ingrese ninguna fuente, su programa deberá seleccionar de forma aleatoria la fuente a utilizar. 
# - Solicite al usuario un texto. 
# - Finalmente, su programa deberá imprimir el texto solicitado usando la fuente apropiada.
"""
Notas: - - - - - - 
Instalar la librería usando:  pip install pyfiglet 
Para usar la librería, debe hacer:  
from pyfiglet import Figlet 
figlet = Figlet() 
Puede obtener la lista de fuentes disponibles usando: figlet.getFonts() 
Para seleccionar el fondo a utilizar emplee: figlet.setFont(font=fuente_seleccionada) 
Finalmente podrá imprimir el texto usando : print(figlet.renderText(texto_imprimir)) 
Recuerde que random tiene un método random choice
"""

import pyfiglet # Importa la librería principal para crear texto ASCII
import random   # Importa la librería para seleccionar un elemento al azar

# --- 1. CONFIGURACIÓN INICIAL DE FIGLET ---
# Creamos el objeto principal de Figlet que usaremos.
figlet = pyfiglet.Figlet()

# Obtenemos la lista de todas las fuentes disponibles.
# Esta lista se guardará para poder elegir una al azar si el usuario no ingresa nada.
fuentes_disponibles = figlet.getFonts()

# --- 2. SOLICITAR LA FUENTE AL USUARIO ---
print("--- GENERADOR DE TEXTO ASCII (FIGlet) ---")
print("Puedes ver ejemplos de fuentes en figlet.org/examples.html")

# Pedimos al usuario que ingrese el nombre de la fuente
fuente_elegida = input("Ingresa el nombre de la fuente (o presiona Enter para elegir una al azar): ")

# Revisamos si el usuario dejó el campo vacío
if not fuente_elegida:
    # Si está vacío, usamos random.choice() para seleccionar una fuente al azar de la lista
    fuente_seleccionada = random.choice(fuentes_disponibles)
    print(f"\nNo se ingresó fuente. Usando fuente aleatoria: '{fuente_seleccionada}'")
else:
    # Si el usuario ingresó algo, verificamos si esa fuente existe
    if fuente_elegida in fuentes_disponibles:
        fuente_seleccionada = fuente_elegida
        print(f"\nUsando la fuente seleccionada: '{fuente_seleccionada}'")
    else:
        # Si el nombre de la fuente es incorrecto, volvemos a elegir una al azar
        print(f"\nADVERTENCIA: La fuente '{fuente_elegida}' no se encontró.")
        fuente_seleccionada = random.choice(fuentes_disponibles)
        print(f"Usando fuente aleatoria en su lugar: '{fuente_seleccionada}'")

# Aplicamos la fuente seleccionada al objeto Figlet
figlet.setFont(font=fuente_seleccionada)

# --- 3. SOLICITAR EL TEXTO AL USUARIO ---
# Pedimos el texto que queremos convertir a ASCII
texto_imprimir = input("\nIngresa el texto que deseas convertir a arte ASCII: ")

# Una comprobación simple para asegurar que hay texto
if not texto_imprimir:
    print("\nERROR: No ingresaste ningún texto. Finalizando programa.")
else:
    # --- 4. IMPRIMIR EL RESULTADO ---
    print("\n" + "="*50)
    print("                  TU ARTE ASCII ")
    print("="*50)

    # Imprimimos el texto usando la fuente seleccionada.
    # El método renderText() es el que hace la magia de dibujar las letras grandes.
    print(figlet.renderText(texto_imprimir))

    print("="*50)
    