import sys
import os

ARCHIVO_CONTADOR = "contador.txt"

def leer_o_inicializar_contador():
    #Si no existe o está vacío, crea contador.txt con 0. Retorna el valor
    if not os.path.exists(ARCHIVO_CONTADOR) or os.path.getsize(ARCHIVO_CONTADOR) == 0:
        guardar_contador(0)
        return 0
    try:
        with open(ARCHIVO_CONTADOR, "r", encoding="utf-8") as f:
            return int(f.read().strip())
    except (ValueError, OSError):
        print("[Aviso] Contenido corrupto en el archivo. Reiniciando a 0.")
        guardar_contador(0)
        return 0

def guardar_contador(valor):
    #Guarda el número en el archivo
    try:
        with open(ARCHIVO_CONTADOR, "w", encoding="utf-8") as f:
            f.write(str(valor))
    except OSError as e:
        print(f"[Error de E/S] No se pudo guardar en {ARCHIVO_CONTADOR}: {e}")

def main():
    # Detecta argumento por línea de comandos o pide entrada por consola
    if len(sys.argv) > 1:
        comando = sys.argv[1].lower().strip()
    else:
        comando = input("Ingrese comando ('inc', 'dec' o ENTER para solo consultar): ").lower().strip()

    valor = leer_o_inicializar_contador()

    if comando == "inc":
        valor += 1
        guardar_contador(valor)
        print(f"Contador incrementado. Nuevo valor: {valor}")
        print(f"Valor actual del contador: {valor}")
    elif comando == "dec":
        valor -= 1
        guardar_contador(valor)
        print(f"Contador decrementado. Nuevo valor: {valor}")
        print(f"Valor actual del contador: {valor}")
    elif comando == "":
        print(f"Valor actual del contador: {valor}")
    else:
        print(f"[Error] Comando '{comando}' no reconocido. Use 'inc', 'dec' o presione ENTER.")

if __name__ == "__main__":
    main()