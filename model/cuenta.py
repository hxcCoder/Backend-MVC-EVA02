# model/cuenta.py
from model.base import BaseModel
from utils.hash_util import HashUtil
from typing import Optional, Dict

class Cuenta(BaseModel):
    def __init__(self, db):
        super().__init__(db, "cuentas")
        
    def crear_cuenta(self, datos: Dict[str, str]) -> bool:
        # Validar campos permitidos
        permitidos = {"username", "password", "rol", "nombre", "apellido", "email"}
        if not set(datos.keys()).issubset(permitidos):
            raise ValueError("Campos inválidos en creación de cuenta")

        datos["password_hash"] = HashUtil.hash_password(datos.pop("password"))
        return self.save(datos)

    def autenticar(self, username: str, password: str) -> Optional[Dict]:
        query = f"SELECT * FROM {self.table} WHERE username = :1"
        result = self.execute_query(query, (username,), fetch=True, as_dict=True)

        if result:
            usuario = result[0]

            if HashUtil.verify_password(password, usuario["PASSWORD_HASH"]):
                return usuario

        return None

    def listar_cuentas(self):
        return self.list_all(as_dict=True)

    def eliminar_cuenta(self, usuario_id: int) -> bool:
        return self.delete(usuario_id)
