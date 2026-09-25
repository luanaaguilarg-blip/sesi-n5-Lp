class Tarea:
    def __init__(self, descripcion, fecha_vencimiento, estado="pendiente"):
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado.lower()  # 'pendiente' o 'completada'

    def a_linea_texto(self):
        return f"{self.descripcion};{self.fecha_vencimiento};{self.estado}\n"

    @classmethod
    def desde_linea_texto(cls, linea):
        partes = linea.strip().split(";")
        return cls(partes[0], partes[1], partes[2])

ARCHIVO_TAREAS = "tareas.txt"

def leer_tareas():
    lista = []
    try:
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as f:
            for linea in f:
                if linea.strip():
                    lista.append(Tarea.desde_linea_texto(linea))
    except FileNotFoundError:
        pass
    return lista

def guardar_todas_tareas(lista):
    try:
        with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as f:
            for t in lista:
                f.write(t.a_linea_texto())
    except IOError as e:
        print(f"Error al guardar tareas: {e}")

def menu_tareas():
    while True:
        print("\n--- GESTOR DE TAREAS PENDIENTES ---")
        print("1. Agregar nueva tarea")
        print("2. Marcar tarea como completada")
        print("3. Listar tareas pendientes")
        print("4. Salir")
        op = input("Elija una opción: ").strip()

        if op == "1":
            desc = input("Descripción de la tarea: ").strip()
            fecha = input("Fecha de vencimiento (ej. 15/10/2026): ").strip()
            if not desc or not fecha:
                print("Error: La descripción y la fecha son obligatorias.")
                continue
            tareas = leer_tareas()
            tareas.append(Tarea(desc, fecha, "pendiente"))
            guardar_todas_tareas(tareas)
            print("Tarea agregada exitosamente.")

        elif op == "2":
            tareas = leer_tareas()
            pendientes = [t for t in tareas if t.estado == "pendiente"]
            if not pendientes:
                print("No hay tareas pendientes para completar.")
                continue

            print("\nSeleccione la tarea a marcar como completada:")
            for idx, t in enumerate(pendientes, 1):
                print(f"  {idx}. {t.descripcion} (Vence: {t.fecha_vencimiento})")

            try:
                seleccion = int(input("Número de tarea: ")) - 1
                if 0 <= seleccion < len(pendientes):
                    pendientes[seleccion].estado = "completada"
                    guardar_todas_tareas(tareas)
                    print("¡Tarea marcada como completada!")
                else:
                    print("Número fuera de rango.")
            except ValueError:
                print("Debe ingresar un número entero.")

        elif op == "3":
            tareas = leer_tareas()
            pendientes = [t for t in tareas if t.estado == "pendiente"]
            print("\n--- Listado de Tareas Pendientes ---")
            if not pendientes:
                print("No tiene tareas pendientes.")
            else:
                for t in pendientes:
                    print(f"• {t.descripcion:<30} | Vence: {t.fecha_vencimiento}")

        elif op == "4":
            print("Saliendo del gestor de tareas...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_tareas()