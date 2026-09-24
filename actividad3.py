def leer_numeros(nombre):
    try:
        archi = open(nombre, "r", encoding="utf-8")
        suma = 0
        contador = 0
        
        ln = archi.readline()
        while ln != "":
            texto_linea = ln.strip()
            
            # Procesa la línea si no está vacía
            if texto_linea != "":
                try:
                    suma += int(texto_linea)
                    contador += 1
                except ValueError:
                    print(f"  [Aviso] La línea '{texto_linea}' no es un número válido.")
            
            # Se lee la siguiente línea fuera del try interno para evitar un bucle infinito
            ln = archi.readline()
            
        archi.close()

        # Validación para evitar división entre cero
        if contador == 0:
            print("[Aviso] No se encontraron números válidos para calcular.")
        else:
            print("\n" + "=" * 35)
            print("El resultado de la suma:     ", suma)
            print("El resultado del promedio: ", suma / contador)
            print("=" * 35)

    except FileNotFoundError:
        print(f"[Error] No existe el archivo llamado '{nombre}'.")
    except PermissionError:
        print(f"[Error] No tiene permisos para leer '{nombre}'.")

def main():
    while True:
        nombre = input("Digite nombre del archivo completo (ejemplo.txt): ").strip()
        if nombre:
            break
        print("[Error] El nombre no puede estar vacío.")
        
    leer_numeros(nombre)

if __name__ == "__main__":
    main()