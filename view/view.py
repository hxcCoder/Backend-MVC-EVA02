def mostrar_menu(usuario):
    print(f"\nBienvenido {usuario.username} - Rol: {usuario.rol}")
    
    if usuario.rol == "admin":
        print("1. Gestionar Usuarios\n2. Gestionar Pacientes\n3. Gestionar Medicos\n0. Salir")
    elif usuario.rol == "paciente":
        print("1. Ver Mis Consultas\n2. Ver Mis Recetas\n0. Salir")
    elif usuario.rol == "medico":
        print("1. Ver Consultas\n2. Registrar Receta\n3. Gestionar Agenda\n0. Salir")
    else:
        print("Rol no definido")
