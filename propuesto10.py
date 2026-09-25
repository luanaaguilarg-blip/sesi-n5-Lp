# --- Jerarquía propia de excepciones ---
class BaseNotasException(Exception):
    #Excepción base para el módulo de procesamiento de notas
    pass

class ArchivoNotasVacioError(BaseNotasException):
    #Lanzada cuando el archivo no contiene líneas de datos
    pass

class FormatoLineaInvalidoError(BaseNotasException):
    #Lanzada cuando una línea no tiene la estructura 'Nombre Apellido Puntos'
    pass

class PuntosNoNumericosError(BaseNotasException):
    #Lanzada cuando la calificación no es un número válido
    pass

def procesar_calificaciones():
    nombre_archivo = input("Ingrese el nombre del archivo de notas: ").strip()
    estudiantes = {}

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        if not lineas:
            raise ArchivoNotasVacioError("El archivo indicado se encuentra vacío.")

        for num_linea, linea in enumerate(lineas, 1):
            linea_limpia = linea.strip()
            if not linea_limpia:
                continue  # Ignorar líneas en blanco
            
            partes = linea_limpia.split()
            if len(partes) < 3:
                raise FormatoLineaInvalidoError(
                    f"Error en la línea {num_linea}: '{linea_limpia}'. Se esperaban al menos 3 elementos (Nombre Apellido Puntos)."
                )

            puntos_str = partes[-1]
            nombre_completo = " ".join(partes[:-1])

            try:
                puntos = float(puntos_str)
            except ValueError:
                raise PuntosNoNumericosError(
                    f"Error en la línea {num_linea}: El valor '{puntos_str}' no es una calificación numérica válida."
                )

            # Acumulación de puntos
            estudiantes[nombre_completo] = estudiantes.get(nombre_completo, 0.0) + puntos

        # Reporte ordenado alfabéticamente
        print("\n" + "="*40)
        print("    REPORTE CONSOLIDADO DE PUNTOS")
        print("="*40)
        for alumno in sorted(estudiantes.keys()):
            print(f"{alumno:<25} : {estudiantes[alumno]:>6.2f} pts")
        print("="*40)

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    except BaseNotasException as e:
        print(f"[EXCEPCIÓN DE NEGOCIO] {e}")
    except Exception as e:
        print(f"[ERROR INESPERADO] {e}")

if __name__ == "__main__":
    procesar_calificaciones()