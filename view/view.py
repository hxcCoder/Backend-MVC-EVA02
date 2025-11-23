# view.py

def mostrar_menu_principal():
    print("\n===== SISTEMA CLÍNICO MEDIPLUS =====")
    print("1. Iniciar sesión")
    print("0. Salir")
    return input("Seleccione una opción: ")


def mostrar_menu(usuario: dict):
    """
    Menú dinámico según el rol del usuario.
    usuario = { username, rol, nombre, apellido, email }
    """

    nombre = usuario.get("nombre", "Usuario")
    rol = usuario.get("rol", "general")

    print(f"\nBienvenido {nombre} - Rol: {rol}\n")

    if rol == "admin":
        print("1. Gestionar Usuarios")
        print("2. Gestionar Pacientes")
        print("3. Gestionar Médicos")
        print("4. Gestionar Insumos")
        print("0. Cerrar sesión")

    elif rol == "paciente":
        print("1. Ver mis datos")
        print("2. Actualizar mis datos")
        print("0. Cerrar sesión")

    elif rol == "medico":
        print("1. Ver pacientes")
        print("2. Actualizar paciente")
        print("3. Gestionar agenda")
        print("0. Cerrar sesión")

    else:
        print("Rol no definido")

    return input("Seleccione una opción: ")


# -------------------------------
# SUBMENÚS
# -------------------------------

def menu_insumos(insumos_controller):
    while True:
        print("\n--- Gestión de Insumos ---")
        print("1. Crear insumo")
        print("2. Listar insumos")
        print("3. Eliminar insumo")
        print("0. Volver")

        op = input("Opción: ")

        if op == "1":
            nombre = input("Nombre: ")
            tipo = input("Tipo: ")
            stock = int(input("Stock: "))

            insumos_controller.crear(nombre, tipo, stock)
            print("✔ Insumo creado exitosamente.")

        elif op == "2":
            datos = insumos_controller.listar()
            print("\n--- LISTA DE INSUMOS ---")
            for fila in datos:
                print(fila)

        elif op == "3":
            id_eliminar = input("ID a eliminar: ")
            insumos_controller.eliminar(int(id_eliminar))
            print("✔ Insumo eliminado.")

        elif op == "0":
            break

        else:
            print("Opción inválida.")
