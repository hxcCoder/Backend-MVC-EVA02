# main.py
from model.cuenta import Cuenta
from model.paciente import Paciente
from model.doctor import Doctor
from config.dbconfig import ConexionOracle

def main():

    # ============================
    # CONEXIÓN A ORACLE
    # ============================
    db = ConexionOracle()
    try:
        db.conectar()
        if not db.connection:
            raise Exception("No se pudo conectar a Oracle")
        print("Conexión exitosa a Oracle")
    except Exception as e:
        print("Error de conexión:", e)
        return

    print("=== Bienvenido al Sistema MediPlus ===")

    # ============================
    # LOGIN
    # ============================
    username = input("Usuario: ")
    password = input("Contraseña: ")

    cuenta_model = Cuenta(db)
    user = cuenta_model.autenticar(username, password)

    if not user:
        print("Usuario o contraseña incorrecta.")
        return

    print(f"¡Bienvenido {user['nombre']}!")

    # ============================
    # MENU SEGÚN ROL
    # ============================
    tipo_usuario = user.get("rol", "general")  # <- CORREGIDO

    while True:
        print("\n--- Menú Principal ---")
        
        if tipo_usuario == "paciente":
            print("1. Ver mis datos")
            print("2. Actualizar mis datos")
        
        elif tipo_usuario == "medico":
            print("1. Ver mis pacientes")
            print("2. Actualizar paciente")
        
        else:  # admin u otros
            print("1. Gestionar Pacientes")
            print("2. Gestionar Médicos")

        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("Saliendo del sistema...")
            break

        # ============================
        # CRUD SIMPLES SEGÚN ROL
        # ============================

        # ---- OPCIÓN 1 ----
        if opcion == "1":
            
            if tipo_usuario == "paciente":
                paciente_model = Paciente(db)
                datos = paciente_model.get_by_id(user["id"])
                print("Tus datos:", datos)

            elif tipo_usuario == "medico":
                paciente_model = Paciente(db)
                pacientes = paciente_model.list_all()
                print("Pacientes:", pacientes)

            else:  # admin
                paciente_model = Paciente(db)
                pacientes = paciente_model.list_all()
                print("Pacientes:", pacientes)

        # ---- OPCIÓN 2 ----
        elif opcion == "2":

            if tipo_usuario == "paciente":
                paciente_model = Paciente(db)
                nuevos_datos = {
                    "nombre": input("Nuevo nombre: "),
                    "apellido": input("Nuevo apellido: "),
                    "email": input("Nuevo email: "),
                    "comuna": input("Nueva comuna: "),
                    "fecha_primera_visita": input("Nueva fecha de primera visita (YYYY-MM-DD): ")
                }
                success = paciente_model.actualizar_cliente(user["id"], nuevos_datos)
                print("Actualización exitosa" if success else "Error al actualizar")

            elif tipo_usuario == "medico":
                paciente_model = Paciente(db)
                pacientes = paciente_model.list_all()

                if pacientes:
                    paciente_id = pacientes[0]["id"]
                    nuevos_datos = {
                        "username": input("Nuevo username: "),
                        "nombre": input("Nuevo nombre: "),
                        "apellido": input("Nuevo apellido: "),
                        "email": input("Nuevo email: "),
                        "comuna": input("Nueva comuna: "),
                        "fecha_primera_visita": input("Nueva fecha primera visita (YYYY-MM-DD): ")
                    }
                    success = paciente_model.actualizar_cliente(paciente_id, nuevos_datos)
                    print("Actualización exitosa" if success else "Error al actualizar")
                else:
                    print("No hay pacientes registrados")

            else:
                print("Función no implementada para este tipo de usuario")

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
