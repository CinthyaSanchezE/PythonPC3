"""
EJERCICIO 1 del MÓDULO 3:
NOMBRE: CINTHYA ELIZABETH SANCHEZ ESPIRITU
"""

# TEMA: Manejo de errores

#PROBLEMA1: Implemente un programa que solicite al usuario una fracción, con formato X/Y, donde cada uno de X e Y es un número entero, 
# y luego muestra, como un porcentaje redondeado al número entero más cercano, donde se indicará la cantidad de combustible en eltanque. 
# Se debe tener en cuenta los siguientes casos:
# Colocar E en caso X/Y sea menor a 1% del total
# Colocar F en caso X/Y sea mayor a 99%. En otro caso, devolver el valor en porcentaje %
# También debe tomar en cuenta los siguientes casos:
# - X y Y deben ser números enteros
# - X debe ser menor o igual a Y, y Y != 0
# De no cumplirse estos casos, se debe volver a preguntar al usuario. Asegúrese de detectar cualquier excepción como ValueError o ZeroDivisionError.
# Ejemplos:
# - Input: 4/0 Acción: Volver a preguntar al usuario dada la excepción ZeroDivisionError
# - Input 1.5/3 Acción: Error dado que solo se permiten números enteros ValueError
# - Input 5/4 Acción: Volver a preguntar al usuario
# - Input 3/4 Output: 75%
# - Input 4/4: Output F
# Nota: Le será de utilidad aplicar try, except ValueError, except ZeroDivisionError

def fraccion_combustible():
    while True:
        try:
            fraccion = input("Ingrese una fracción en el formato X/Y (donde X e Y son números enteros): ")
            x_str, y_str = fraccion.split('/')
            x = int(x_str)
            y = int(y_str)
            
            if y == 0:
                raise ZeroDivisionError("El denominador no puede ser cero. Intente de nuevo.")
            if x > y:
                print("Error: X debe ser menor o igual a Y. Intente de nuevo.")
                continue
            
            porcentaje = (x / y) * 100
            
            if porcentaje < 1:
                return "E"
            elif porcentaje > 99:
                return "F"
            else:
                return f"{round(porcentaje)}%"
        
        except ValueError:
            print("Error: Asegúrese de ingresar números enteros en el formato correcto. Intente de nuevo.")
        except ZeroDivisionError as zde:
            print(zde)
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}. Intente de nuevo.")
if __name__ == "__main__":
    resultado = fraccion_combustible()
    print(f"Resultado: {resultado}")


