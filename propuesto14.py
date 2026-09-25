class Habitacion:
    def __init__(self, numero_de_habitacion, tipo_habitacion, precio_por_noche):
        self.numero_de_habitacion = str(numero_de_habitacion)
        self.tipo_habitacion = tipo_habitacion
        self.precio_por_noche = float(precio_por_noche)

ARCHIVO_RESERVAS = "reservas.txt"

# Inventario de habitaciones del hotel
CATALOGO_HABITACIONES = [
    Habitacion("101", "Simple", 60.0),
    Habitacion("102", "Simple", 60.0),
    Habitacion("201", "Doble", 100.0),
    Habitacion("202", "Doble", 100.0),
    Habitacion("301", "Matrimonial", 140.0),
    Habitacion("401", "Suite Presidencial", 250.0),
]

def obtener_reservas():
    #Lee reservas del archivo 'reservas.txt'
    reservas = []
    try:
        with open(ARCHIVO_RESERVAS, "r", encoding="utf-8") as f:
            for l in f:
                if l.strip():
                    cliente, num_hab, noches, total = l.strip().split(";")
                    reservas.append({
                        "cliente": cliente,
                        "num_hab": num_hab,
                        "noches": int(noches),
                        "total": float(total)
                    })
    except FileNotFoundError:
        pass
    return reservas

def menu_hotel():
    while True:
        print("\n" + "="*40)
        print("    SISTEMA DE RESERVAS - HOTEL")
        print("="*40)
        print("1. Verificar disponibilidad")
        print("2. Realizar una reserva")
        print("3. Generar factura para un cliente")
        print("4. Salir")
        op = input("Seleccione una opción: ").strip()

        if op == "1":
            reservas = obtener_reservas()
            habs_ocupadas = [r["num_hab"] for r in reservas]
            print("\n--- Estado de Habitaciones ---")
            for hab in CATALOGO_HABITACIONES:
                estado = "OCUPADA" if hab.numero_de_habitacion in habs_ocupadas else "DISPONIBLE"
                print(f"Hab #{hab.numero_de_habitacion:<3} | {hab.tipo_habitacion:<18} | S/. {hab.precio_por_noche:>6.2f}/noche -> [{estado}]")

        elif op == "2":
            reservas = obtener_reservas()
            habs_ocupadas = [r["num_hab"] for r in reservas]
            
            num = input("Ingrese el número de habitación a reservar: ").strip()
            hab_seleccionada = next((h for h in CATALOGO_HABITACIONES if h.numero_de_habitacion == num), None)

            if not hab_seleccionada:
                print("Error: El número de habitación no existe en el hotel.")
            elif num in habs_ocupadas:
                print("Error: La habitación seleccionada ya se encuentra ocupada.")
            else:
                cliente = input("Nombre completo del cliente: ").strip()
                if not cliente:
                    print("Error: El nombre del cliente no puede estar vacío.")
                    continue
                try:
                    noches = int(input("Cantidad de noches a hospedarse: "))
                    if noches <= 0:
                        print("Error: Las noches deben ser un número positivo.")
                        continue
                    
                    total = noches * hab_seleccionada.precio_por_noche
                    with open(ARCHIVO_RESERVAS, "a", encoding="utf-8") as f:
                        f.write(f"{cliente};{num};{noches};{total}\n")
                    
                    print(f"¡Reserva confirmada con éxito! Total a pagar: S/. {total:.2f}")
                except ValueError:
                    print("Error: Debe ingresar una cantidad de noches válida.")

        elif op == "3":
            cliente_buscar = input("Ingrese el nombre del cliente: ").strip().lower()
            reservas = obtener_reservas()
            reserva_cliente = next((r for r in reservas if r["cliente"].lower() == cliente_buscar), None)

            if reserva_cliente:
                hab_info = next((h for h in CATALOGO_HABITACIONES if h.numero_de_habitacion == reserva_cliente["num_hab"]), None)
                tipo = hab_info.tipo_habitacion if hab_info else "Estándar"
                
                print("\n" + "="*35)
                print("         FACTURA DE HOTEL")
                print("="*35)
                print(f"Cliente:      {reserva_cliente['cliente']}")
                print(f"Habitación:   #{reserva_cliente['num_hab']} ({tipo})")
                print(f"Noches:       {reserva_cliente['noches']}")
                print(f"Total a Pagar: S/. {reserva_cliente['total']:.2f}")
                print("="*35)
            else:
                print(f"No se encontraron reservas registradas a nombre de '{cliente_buscar}'.")

        elif op == "4":
            print("Cerrando el sistema del hotel...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_hotel()