def pedir_entero_rango(min_v=1, max_v=10):
    while True:
        entrada = input(f"Ingrese un número entero del {min_v} al {max_v}: ").strip()
        try:
            num = int(entrada)
            if min_v <= num <= max_v:
                return num
            print(f"[Aviso] El número debe estar estrictamente entre {min_v} y {max_v}.")
        except ValueError:
            print("[Error] Entrada inválida. Ingrese solo números enteros.")

def main():
    numero = pedir_entero_rango(1, 10)
    nombre_archivo = "tabla_propuesto.txt"

    try:
        # 1. Escritura de la tabla en el archivo
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write(f"TABLA DE MULTIPLICAR DEL {numero}\n")
            f.write("=" * 30 + "\n")
            for i in range(1, 13):
                f.write(f"{numero} x {i:2d} = {numero * i}\n")
        
        print(f"\n[Éxito] Se guardó la tabla en '{nombre_archivo}'.")
        
        # 2. Lectura y confirmación en pantalla
        print("\n--- Vista previa del archivo generado ---")
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            print(f.read().strip())

    except OSError as e:
        print(f"[Error al manipular el archivo] {e}")

if __name__ == "__main__":
    main()