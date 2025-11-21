from base import BaseModel
from utils.hash_util import HashUtil

class Cuenta(BaseModel):
    def __init__(self, db):
        super().__init__(db, "cuentas")  # Tabla en BD
        self.usuario_id = None
        self.username = None
        self.password_hash = None
        self.rol = None  # Admin, Doctor, Cliente
        self.nombre = None
        self.apellido = None
        self.email = None

    # ---------------------------
    # CREAR CUENTA
    # ---------------------------
    def crear_cuenta(self, datos: dict) -> bool:
        """
        Espera diccionario: 
        {'username': str, 'password': str, 'rol': str, 'nombre': str, 'apellido': str, 'email': str}
        """
        # Generar hash de la contraseña
        datos["password_hash"] = HashUtil.hash_password(datos.pop("password"))
        return self.save(datos)

    # ---------------------------
    # LOGIN
    # ---------------------------
    def login(self, username: str, password: str):
        query = f"SELECT * FROM {self.table} WHERE username = :1"
        result = self.execute_query(query, (username,), fetch=True)
        if result:
            usuario = result[0]
            if HashUtil.verify_password(password, usuario[2]):  # asumiendo password_hash está en la columna 3
                return usuario  # Devuelve datos del usuario
        return None

    # ---------------------------
    # LISTAR CUENTAS
    # ---------------------------
    def listar_cuentas(self):
        return self.list_all()

    # ---------------------------
    # ELIMINAR CUENTA
    # ---------------------------
    def eliminar_cuenta(self, usuario_id: int) -> bool:
        return self.delete(usuario_id)
