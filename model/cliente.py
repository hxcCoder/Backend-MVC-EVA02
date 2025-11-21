from cuenta import Cuenta

class Cliente(Cuenta):
    def __init__(self, db):
        super().__init__(db)
        self.comuna = None
        self.fecha_primera_visita = None

    # ---------------------------
    # CREAR CLIENTE
    # ---------------------------
    def crear_cliente(self, datos: dict) -> bool:
        """
        Espera diccionario con claves:
        {'username', 'password', 'rol', 'nombre', 'apellido', 'email', 'comuna', 'fecha_primera_visita'}
        """
        return super().crear_cuenta(datos)  # Reutiliza crear_cuenta para hash y guardado

    # ---------------------------
    # ACTUALIZAR CLIENTE
    # ---------------------------
def actualizar_cliente(self, usuario_id: int, datos: dict) -> bool:
    try:
        query = f"""
        UPDATE {self.table} SET 
            username = :1, nombre = :2, apellido = :3, email = :4, 
            comuna = :5, fecha_primera_visita = :6
        WHERE id = :7
        """
        params = (
            datos.get("username"),
            datos.get("nombre"),
            datos.get("apellido"),
            datos.get("email"),
            datos.get("comuna"),
            datos.get("fecha_primera_visita"),
            usuario_id
        )
        self.execute_query(query, params)  # Ejecuta la query
        return True                        # Siempre retorna bool
    except Exception as e:
        print("Error al actualizar cliente:", e)
        return False


    # ---------------------------
    # LISTAR CLIENTES
    # ---------------------------
    def listar_clientes(self):
        return super().listar_cuentas()

    # ---------------------------
    # OBTENER CLIENTE POR ID
    # ---------------------------
    def obtener_cliente(self, usuario_id: int):
        return super().get_by_id(usuario_id)
