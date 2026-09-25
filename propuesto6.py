import os

def contar_frecuencia_palabras():
    nombre_archivo = input("Ingrese el nombre del archivo con su extensión (ej. texto.txt): ").strip()
    
    try:
        # Validar existencia antes de abrir
        if not os.path.exists(nombre_archivo):
            raise FileNotFoundError(f"El archivo '{nombre_archivo}' no existe en el directorio.")
        
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            contenido = f.read()

        # Separar palabras eliminando signos de puntuación comunes
        palabras_brutas = contenido.split()
        if not palabras_brutas:
            print("El archivo está vacío.")
            return

        diccionario_frecuencias = {}
        for p in palabras_brutas:
            # Limpieza básica de signos de puntuación y paso a minúsculas
            palabra_limpia = p.strip(".,;:¡!¿?()\"'[]{}«»\n\t").lower()
            if palabra_limpia:
                diccionario_frecuencias[palabra_limpia] = diccionario_frecuencias.get(palabra_limpia, 0) + 1

        print("\n--- Conteo de Palabras ---")
        for palabra, cantidad in diccionario_frecuencias.items():
            print(f"{palabra}: {cantidad}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError:
        print("Error: No tiene permisos para leer el archivo.")
    except Exception as e:
        print(f"Ocurrió un error imprevisto: {e}")

if __name__ == "__main__":
    contar_frecuencia_palabras()