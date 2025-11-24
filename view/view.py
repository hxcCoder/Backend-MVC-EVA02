# view.py

def menu_usuarios(usuarios_controller):
    while True:
        print("\n--- Gestión de Usuarios ---")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("0. Volver")

        op = input("Opción: ")

        # Crear usuario
        if op == "1":
            print("\n--- Crear Usuario ---")
            username = input("Username: ")
            password = input("Password: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            email = input("Email: ")
            rol = input("Rol (admin/medico/paciente): ")

            usuarios_controller.crear(username, password, nombre, apellido, email, rol)
            print("✔ Usuario creado exitosamente.")

        # Listar usuarios
        elif op == "2":
            print("\n--- Lista de Usuarios ---")
            usuarios = usuarios_controller.listar()
            for u in usuarios:
                print(u)

        # Actualizar usuario
        elif op == "3":
            print("\n--- Actualizar Usuario ---")
            user_id = int(input("ID del usuario: "))
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_apellido = input("Nuevo apellido: ")
            nuevo_email = input("Nuevo email: ")
            nuevo_rol = input("Nuevo rol: ")

            usuarios_controller.actualizar(
                user_id, nuevo_nombre, nuevo_apellido, nuevo_email, nuevo_rol
            )
            print("✔ Usuario actualizado.")

        # Eliminar usuario
        elif op == "4":
            print("\n--- Eliminar Usuario ---")
            user_id = int(input("ID del usuario: "))
            usuarios_controller.eliminar(user_id)
            print("✔ Usuario eliminado.")

        elif op == "0":
            break

        else:
            print("Opción inválida.")
