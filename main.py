# main.py
from model.cuenta import Cuenta
from model.paciente import Paciente
from model.doctor import Doctor
from config.dbconfig import ConexionOracle

def main():
    # Conexión a la base de datos
    db = ConexionOracle()

    print("=== Bienvenido al Sistema MediPlus ===")

    # Login simple
    username = input("Usuario: ")
    password = input("Contraseña: ")

    cuenta_model = Cuenta(db)
    user = cuenta_model.autenticar(username, password)



    if not user:
        print("Usuario o contraseña incorrecta.")
        return

    print(f"¡Bienvenido {user['nombre']}!")

    # Menú según tipo de usuario
    tipo_usuario = user.get("tipo", "general")

    while True:
        print("\n--- Menú Principal ---")
        if tipo_usuario == "paciente":
            print("1. Ver mis datos")
            print("2. Actualizar mis datos")
        elif tipo_usuario == "medico":
            print("1. Ver mis pacientes")
            print("2. Actualizar paciente")
        else:
            print("1. Gestionar Pacientes")
            print("2. Gestionar Médicos")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("Saliendo del sistema...")
            break

        # Aquí podrías agregar llamadas a métodos CRUD según el modelo
        if opcion == "1":
            if tipo_usuario == "paciente":
                paciente_model = Paciente(db)
                datos = paciente_model.get_by_id(user["id"])
                print("Tus datos:", datos)
            elif tipo_usuario == "medico":
                paciente_model = Paciente(db)
                pacientes = paciente_model.list_all()
                print("Pacientes:", pacientes)
            else:
                paciente_model = Paciente(db)
                pacientes = paciente_model.list_all()
                print("Pacientes:", pacientes)
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
                # Para simplificar, actualizamos el primer paciente
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
            print("Opción no válida")

if __name__ == "__main__":
    main()
