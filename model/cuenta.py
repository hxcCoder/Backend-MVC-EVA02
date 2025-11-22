# model/cuenta.py
from model.base import BaseModel
from utils.hash_util import HashUtil
from typing import Optional, Dict

class Cuenta(BaseModel):
    def __init__(self, db):
        super().__init__(db, "cuentas")  # Tabla en BD
        self.usuario_id: Optional[int] = None
        self.username: Optional[str] = None
        self.password_hash: Optional[str] = None
        self.rol: Optional[str] = None  # Admin, Doctor, Cliente
        self.nombre: Optional[str] = None
        self.apellido: Optional[str] = None
        self.email: Optional[str] = None

    # ---------------------------
    # CREAR CUENTA
    # ---------------------------
    def crear_cuenta(self, datos: Dict[str, str]) -> bool:
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
    def autenticar(self, username: str, password: str) -> Optional[Dict]:
        """
        Devuelve datos del usuario si login correcto, None si falla.
        """
        query = f"SELECT * FROM {self.table} WHERE username = :1"
        result = self.execute_query(query, (username,), fetch=True)
        if result:
            usuario = result[0]
            if HashUtil.verify_password(password, usuario[2]):  # asumiendo password_hash está en la columna 3
                return {
                    "usuario_id": usuario[0],
                    "username": usuario[1],
                    "rol": usuario[3],
                    "nombre": usuario[4],
                    "apellido": usuario[5],
                    "email": usuario[6]
                }
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
