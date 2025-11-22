# view.py

def mostrar_menu(usuario: dict):
    """
    Muestra el menú según el rol del usuario.
    Usuario debe ser un diccionario con claves:
    'username', 'rol', 'nombre', 'apellido', 'email', etc.
    """
    nombre = usuario.get("nombre", "Usuario")
    rol = usuario.get("rol", "general")
    
    print(f"\nBienvenido {nombre} - Rol: {rol}\n")
    
    if rol == "admin":
        print("1. Gestionar Usuarios")
        print("2. Gestionar Pacientes")
        print("3. Gestionar Médicos")
        print("0. Salir")
    elif rol == "paciente":
        print("1. Ver Mis Datos")
        print("2. Actualizar Mis Datos")
        print("0. Salir")
    elif rol == "medico":
        print("1. Ver Pacientes")
        print("2. Actualizar Paciente")
        print("3. Gestionar Agenda")
        print("0. Salir")
    else:
        print("Rol no definido")
