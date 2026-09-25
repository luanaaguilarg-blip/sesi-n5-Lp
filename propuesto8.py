import os

ARCHIVO_AGENDA = "agenda.txt"

def cargar_contactos():
    #Lee el archivo agenda.txt y retorna un diccionario: {nombre_min: [nombre_orig, telefono]}
    contactos = {}
    if os.path.exists(ARCHIVO_AGENDA):
        try:
            with open(ARCHIVO_AGENDA, "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if ";" in linea:
                        nombre, tel = linea.split(";", 1)
                        contactos[nombre.lower()] = [nombre, tel]
        except IOError as e:
            print(f"Error al leer la agenda: {e}")
    return contactos

def guardar_contactos(contactos):
    #Guarda todos los contactos en agenda.txt
    try:
        with open(ARCHIVO_AGENDA, "w", encoding="utf-8") as f:
            for datos in contactos.values():
                f.write(f"{datos[0]};{datos[1]}\n")
    except IOError as e:
        print(f"Error al guardar los cambios: {e}")

def menu_agenda():
    while True:
        print("\n" + "="*35)
        print("        AGENDA TELEFÓNICA")
        print("="*35)
        print("1. Consultar un celular")
        print("2. Añadir un celular")
        print("3. Eliminar un celular")
        print("4. Crear la agenda")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            if not os.path.exists(ARCHIVO_AGENDA):
                print("Aviso: La agenda aún no ha sido creada.")
                continue
            nombre = input("Ingrese el nombre del cliente a consultar: ").strip()
            contactos = cargar_contactos()
            if nombre.lower() in contactos:
                print(f"-> Cliente: {contactos[nombre.lower()][0]} | Celular: {contactos[nombre.lower()][1]}")
            else:
                print(f"No existe el cliente '{nombre}' en la agenda.")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del cliente: ").strip()
            celular = input("Ingrese el número de celular: ").strip()
            if not nombre or not celular:
                print("Error: El nombre y el celular no pueden estar vacíos.")
                continue
            contactos = cargar_contactos()
            contactos[nombre.lower()] = [nombre, celular]
            guardar_contactos(contactos)
            print(f"Registro guardado con éxito para '{nombre}'.")

        elif opcion == "3":
            if not os.path.exists(ARCHIVO_AGENDA):
                print("Aviso: La agenda no existe.")
                continue
            nombre = input("Ingrese el nombre del cliente que desea eliminar: ").strip()
            contactos = cargar_contactos()
            if nombre.lower() in contactos:
                del contactos[nombre.lower()]
                guardar_contactos(contactos)
                print(f"El cliente '{nombre}' ha sido eliminado.")
            else:
                print(f"No se encontró al cliente '{nombre}' en la agenda.")

        elif opcion == "4":
            if os.path.exists(ARCHIVO_AGENDA):
                confirmacion = input("El archivo ya existe. ¿Desea eliminarlo y empezar uno nuevo? (s/n): ").strip().lower()
                if confirmacion == 's':
                    open(ARCHIVO_AGENDA, "w", encoding="utf-8").close()
                    print("Se ha reiniciado el archivo 'agenda.txt'.")
                else:
                    print("Operación cancelada.")
            else:
                open(ARCHIVO_AGENDA, "w", encoding="utf-8").close()
                print("Archivo 'agenda.txt' creado exitosamente.")

        elif opcion == "5":
            print("Cerrando la agenda. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Ingrese un número del 1 al 5.")

if __name__ == "__main__":
    menu_agenda()