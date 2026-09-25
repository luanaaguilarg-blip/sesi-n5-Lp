import os

def procesar_vocales(texto):
    #Cuenta y desglosa las vocales del texto ingresado
    mapeo = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u'}
    conteo = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    total = 0

    for caracter in texto.lower():
        c_norm = mapeo.get(caracter, caracter)
        if c_norm in conteo:
            conteo[c_norm] += 1
            total += 1

    return total, conteo

def opcion_1_cadena():
    print("\n--- [OPCIÓN 1] LEER CADENA DE CARACTERES ---")
    while True:
        oracion = input("Ingrese una oración: ").strip()
        if oracion:
            break
        print("[Error] El texto no puede estar vacío.")

    total, desglose = procesar_vocales(oracion)

    # Guardar reporte en vocales.txt
    try:
        with open("vocales.txt", "w", encoding="utf-8") as f:
            f.write("REPORTE DE VOCALES ENCONTRADAS\n")
            f.write("=" * 30 + "\n")
            f.write(f"Texto analizado : {oracion}\n")
            f.write(f"Total vocales   : {total}\n")
            for v, cantidad in desglose.items():
                f.write(f"  Vocal '{v.upper()}/{v}': {cantidad}\n")

        print("\n[Éxito] Reporte guardado en 'vocales.txt'.")
        print("Contenido del archivo:")
        with open("vocales.txt", "r", encoding="utf-8") as f:
            print(f.read())
            
    except OSError as e:
        print(f"[Error al escribir vocales.txt] {e}")

def opcion_2_archivo():
    print("\n--- [OPCIÓN 2] LEER DESDE ARCHIVO ---")
    nombre = input("Ingrese el nombre del archivo (con extensión): ").strip()

    if not os.path.exists(nombre):
        print(f"[Error] El archivo '{nombre}' no fue encontrado.")
        return

    try:
        with open(nombre, "r", encoding="utf-8") as f:
            contenido = f.read()

        total, desglose = procesar_vocales(contenido)
        print("\n" + "=" * 35)
        print(f"Archivo analizado : {nombre}")
        print(f"Total de vocales  : {total}")
        for v, cantidad in desglose.items():
            print(f"  - Vocal '{v.upper()}/{v}': {cantidad}")
        print("=" * 35)

    except PermissionError:
        print("[Error] No tiene permisos para leer el archivo.")
    except UnicodeDecodeError:
        print("[Error] Formato de texto incompatible (se requiere UTF-8).")
    except OSError as e:
        print(f"[Error de E/S] {e}")

def menu():
    while True:
        print("\n==============================")
        print("       MENÚ DE VOCALES")
        print("==============================")
        print("1. Leer cadena de caracteres")
        print("2. Leer archivo")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1-3): ").strip()

        if opcion == "1":
            opcion_1_cadena()
        elif opcion == "2":
            opcion_2_archivo()
        elif opcion == "3":
            print("\nPrograma finalizado correctamente.")
            break
        else:
            print("[Error] Opción no válida. Ingrese 1, 2 o 3.")

if __name__ == "__main__":
    menu()