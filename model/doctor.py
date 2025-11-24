from model.cuenta import Cuenta

class Doctor:
    def __init__(self, db):
        self.db = db
        self.cuenta = Cuenta(db)  # Composición en vez de herencia

    # ---------------------------
    # CREAR DOCTOR
    # ---------------------------
    def crear_doctor(self, datos: dict) -> bool:
        """
        Datos esperados:
        username, password, nombre, apellido, email, especialidad, horario_atencion, fecha_ingreso
        """

        # 1. Crear la cuenta base (rol = "medico")
        cuenta_info = {
            "username": datos["username"],
            "password": datos["password"],
            "rol": "medico",
            "nombre": datos["nombre"],
            "apellido": datos["apellido"],
            "email": datos["email"]
        }

        id_cuenta = self.cuenta.crear_cuenta_retornando_id(cuenta_info)
        if not id_cuenta:
            return False

        # 2. Insertar datos específicos de doctor
        cursor = self.db.obtener_cursor()
        cursor.execute("""
            INSERT INTO doctor (id_cuenta, especialidad, horario_atencion, fecha_ingreso)
            VALUES (:1, :2, :3, :4)
        """, (
            id_cuenta,
            datos["especialidad"],
            datos["horario_atencion"],
            datos["fecha_ingreso"]
        ))

        self.db.connection.commit()
        return True

    # ---------------------------
    # LISTAR DOCTORES
    # ---------------------------
    def listar_doctores(self):
        cursor = self.db.obtener_cursor()
        cursor.execute("""
            SELECT 
                d.id_doctor,
                c.username,
                c.nombre,
                c.apellido,
                c.email,
                d.especialidad,
                d.horario_atencion,
                d.fecha_ingreso
            FROM doctor d
            JOIN cuenta c ON c.id = d.id_cuenta
        """)

        return [dict(zip([c[0] for c in cursor.description], fila)) for fila in cursor]

    # ---------------------------
    # OBTENER DOCTOR
    # ---------------------------
    def obtener_doctor(self, id_doctor):
        cursor = self.db.obtener_cursor()
        cursor.execute("""
            SELECT 
                d.id_doctor,
                c.id AS id_cuenta,
                c.username,
                c.nombre,
                c.apellido,
                c.email,
                d.especialidad,
                d.horario_atencion,
                d.fecha_ingreso
            FROM doctor d
            JOIN cuenta c ON c.id = d.id_cuenta
            WHERE d.id_doctor = :1
        """, (id_doctor,))

        fila = cursor.fetchone()
        return dict(zip([c[0] for c in cursor.description], fila)) if fila else None
