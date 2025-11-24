from model.cuenta import Cuenta
from model.paciente import Paciente
from model.doctor import Doctor
from config.dbconfig import ConexionOracle

def main():

    # -----------------------------
    # CONEXIÓN A ORACLE
    # -----------------------------
    db = ConexionOracle()
    try:
        db.conectar()
        if not db.connection:
            raise Exception("No se pudo conectar a Oracle")
        print("Conexión exitosa a Oracle")
    except Exception as e:
        print("Error de conexión:", e)
        return

    cuenta_model = Cuenta(db)

    print("=== Bienvenido al Sistema MediPlus ===")

    # -----------------------------
    # MENÚ INICIAL
    # -----------------------------
    user = None
    tipo_usuario = None

    while True:
        print("\n1) Iniciar sesión")
        print("2) Registrarse (solo paciente)")
        print("0) Salir")
        opcion_inicio = input("Seleccione una opción: ")

        # ---- SALIR ----
        if opcion_inicio == "0":
            print("Saliendo del sistema...")
            return

        # ---- REGISTRO (seguro) ----
        if opcion_inicio == "2":
            print("\n=== Registro de nuevo paciente ===")

            datos = {
                "username": input("Nuevo username: "),
                "password": input("Contraseña: "),
                "rol": "paciente",   # 🔐 Seguridad: NO permitir admin ni médico aquí
                "nombre": input("Nombre: "),
                "apellido": input("Apellido: "),
                "email": input("Email: ")
            }

            exito = cuenta_model.crear_cuenta(datos)
            print("✔ Registro exitoso. Ahora inicie sesión." if exito else "✖ Error al registrar.")
            continue

        # ---- LOGIN ----
        if opcion_inicio == "1":
            username = input("Usuario: ")
            password = input("Contraseña: ")

            user = cuenta_model.autenticar(username, password)

            if not user:
                print("✖ Usuario o contraseña incorrecta.")
                continue

            print(f"\n✔ Bienvenido {user['nombre']} ({user['rol']})")
            tipo_usuario = user["rol"]
            break

        print("Opción inválida.")

    # ------------------------------------------------
    # MENU PRINCIPAL (tras login)
    # ------------------------------------------------
    while True:
        print("\n--- Menú Principal ---")

        if tipo_usuario == "paciente":
            print("1. Ver mis datos")
            print("2. Actualizar mis datos")

        elif tipo_usuario == "medico":
            print("1. Ver pacientes")
            print("2. Actualizar paciente")

        elif tipo_usuario == "admin":
            print("1. Crear usuario")
            print("2. Gestionar pacientes")
            print("3. Gestionar médicos")

        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("Cerrando sesión...")
            break

        # ==================================================
        # OPCIÓN 1
        # ==================================================
        if opcion == "1":

            # --- PACIENTE ---
            if tipo_usuario == "paciente":
                paciente_model = Paciente(db)
                datos = paciente_model.get_by_id(user["usuario_id"])
                print("\n=== MIS DATOS ===")
                print(datos)
            
            # --- MÉDICO ---
            elif tipo_usuario == "medico":
                paciente_model = Paciente(db)
                pacientes = paciente_model.list_all()
                print("\n=== Pacientes ===")
                print(pacientes)

            # --- ADMIN CREA USUARIO ---
            elif tipo_usuario == "admin":
                print("\n=== Crear Usuario ===")
                datos = {
                    "username": input("Nuevo username: "),
                    "password": input("Password: "),
                    "nombre": input("Nombre: "),
                    "apellido": input("Apellido: "),
                    "email": input("Email: "),
                    "rol": input("Rol (admin/medico/paciente): ")  # 👈 aquí sí se permite admin
                }
                cuenta_model.crear_cuenta(datos)
                print("✔ Usuario creado exitosamente!")

        # ==================================================
        # OPCIÓN 2
        # ==================================================
        elif opcion == "2":

            # --- PACIENTE ACTUALIZA SUS DATOS ---
            if tipo_usuario == "paciente":
                paciente_model = Paciente(db)
                nuevos_datos = {
                    "nombre": input("Nuevo nombre: "),
                    "apellido": input("Nuevo apellido: "),
                    "email": input("Nuevo email: "),
                    "comuna": input("Nueva comuna: "),
                    "fecha_primera_visita": input("Nueva fecha (YYYY-MM-DD): ")
                }
                success = paciente_model.actualizar_cliente(user["usuario_id"], nuevos_datos)
                print("Actualizado correctamente" if success else "Error al actualizar")

            # --- MÉDICO ACTUALIZA PACIENTE ---
            elif tipo_usuario == "medico":
                paciente_model = Paciente(db)
                pacientes = paciente_model.list_all()

                if not pacientes:
                    print("No hay pacientes registrados.")
                    continue

                paciente_id = pacientes[0]["id"]
                nuevos = {
                    "username": input("Nuevo username: "),
                    "nombre": input("Nuevo nombre: "),
                    "apellido": input("Nuevo apellido: "),
                    "email": input("Nuevo email: "),
                    "comuna": input("Nueva comuna: "),
                    "fecha_primera_visita": input("Nueva fecha (YYYY-MM-DD): ")
                }
                success = paciente_model.actualizar_cliente(paciente_id, nuevos)
                print("Actualizado correctamente" if success else "Error al actualizar")

            # --- ADMIN: LISTAR PACIENTES ---
            elif tipo_usuario == "admin":
                paciente_model = Paciente(db)
                pacientes = paciente_model.list_all()
                print("\n=== Pacientes ===")
                print(pacientes)

        # ==================================================
        # OPCIÓN 3 (solo admin)
        # ==================================================
        elif opcion == "3" and tipo_usuario == "admin":
            doctor_model = Doctor(db)
            doctores = doctor_model.list_all()
            print("\n=== Doctores ===")
            print(doctores)

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
