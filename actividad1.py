def actividad_1():
    print("=== ACTIVIDAD 1: CREACIÓN Y ESCRITURA DE ARCHIVO ===")
    
    # 1. Validación del nombre del archivo
    while True:
        nombre = input("Ingrese el nombre del archivo a crear (ej. archivo.txt): ").strip()
        if not nombre:
            print("[Error] El nombre no puede estar vacío.")
            continue
        if not nombre.endswith(".txt"):
            nombre += ".txt"
        break

    # 2. Validación del contenido a escribir
    while True:
        linea = input("Ingrese el texto que desea insertar: ").strip()
        if not linea:
            print("[Error] Debe ingresar algún texto.")
            continue
        break

    # 3. Apertura en modo escritura ('w') y cierre automático
    try:
        with open(nombre, "w", encoding="utf-8") as archi:
            archi.write(linea + "\n")
        print(f"\n[Éxito] Se creó '{nombre}' e insertó la línea correctamente.")
        
    except PermissionError:
        print("[Error] Permiso denegado para escribir en esta ubicación.")
    except OSError as e:
        print(f"[Error de E/S] Ocurrió un error al guardar: {e}")

if __name__ == "__main__":
    actividad_1()