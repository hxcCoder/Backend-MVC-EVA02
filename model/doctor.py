from model.cuenta import Cuenta

class Doctor(Cuenta):
    def __init__(self, db):
        super().__init__(db)
        self.especialidad = None
        self.horario_atencion = None
        self.fecha_ingreso = None

    # ---------------------------
    # CREAR DOCTOR
    # ---------------------------
    def crear_doctor(self, datos: dict) -> bool:
        """
        Espera diccionario con claves:
        {'username', 'password', 'rol', 'nombre', 'apellido', 'email', 
         'especialidad', 'horario_atencion', 'fecha_ingreso'}
        """
        return super().crear_cuenta(datos)

    # ---------------------------
    # ACTUALIZAR DOCTOR
    # ---------------------------
    def actualizar_doctor(self, usuario_id: int, datos: dict) -> bool:
        query = f"""
        UPDATE {self.table} SET 
        username = :1, nombre = :2, apellido = :3, email = :4, 
        especialidad = :5, horario_atencion = :6, fecha_ingreso = :7
        WHERE id = :8
        """
        params = (
            datos.get("username"),
            datos.get("nombre"),
            datos.get("apellido"),
            datos.get("email"),
            datos.get("especialidad"),
            datos.get("horario_atencion"),
            datos.get("fecha_ingreso"),
            usuario_id
        )
        self.execute_query(query, params)
        return True

    # ---------------------------
    # LISTAR DOCTORES
    # ---------------------------
    def listar_doctores(self):
        return super().listar_cuentas()

    # ---------------------------
    # OBTENER DOCTOR POR ID
    # ---------------------------
    def obtener_doctor(self, usuario_id: int):
        return super().get_by_id(usuario_id)
