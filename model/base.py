# model/base.py
from typing import Any, Dict, Tuple, List
import hashlib

class BaseModel:
    """
    Clase base para todos los modelos.
    Maneja CRUD básico y login simple.
    """

    def __init__(self, db, table: str):
        self.db = db
        self.table = table

    # ---------------------------
    # Ejecuta cualquier query SQL
    # ---------------------------
    def execute_query(self, query: str, params: Tuple = (), fetch: bool = False):
        if not self.db.connection:
            self.db.conectar()

        cursor = self.db.obtener_cursor()
        cursor.execute(query, params)

        if fetch:
            rows = cursor.fetchall()
            return rows if rows else []

        self.db.connection.commit()
        return []

    # ---------------------------
    # Crear registro
    # ---------------------------
    def save(self, data: Dict[str, Any]) -> bool:
        try:
            columns = ", ".join(data.keys())
            placeholders = ", ".join([f":{i+1}" for i in range(len(data))])
            params = tuple(data.values())
            query = f"INSERT INTO {self.table} ({columns}) VALUES ({placeholders})"
            self.execute_query(query, params)
            return True
        except Exception as e:
            print("Error al guardar:", e)
            return False

    # ---------------------------
    # Buscar por ID
    # ---------------------------
    def get_by_id(self, record_id: int):
        query = f"SELECT * FROM {self.table} WHERE id = :1"
        rows = self.execute_query(query, (record_id,), fetch=True)
        return rows[0] if rows else None

    # ---------------------------
    # Listar todos los registros
    # ---------------------------
    def list_all(self) -> List[Dict[str, Any]]:
        query = f"SELECT * FROM {self.table}"
        return self.execute_query(query, fetch=True)

    # ---------------------------
    # Eliminar por ID
    # ---------------------------
    def delete(self, record_id: int) -> bool:
        try:
            query = f"DELETE FROM {self.table} WHERE id = :1"
            self.execute_query(query, (record_id,))
            return True
        except Exception as e:
            print("Error al eliminar:", e)
            return False

    # ---------------------------
    # Login simple
    # ---------------------------
    def login(self, username_col: str, username: str, password_col: str, password: str):
        hashed_password = self.hash_password(password)
        query = f"SELECT * FROM {self.table} WHERE {username_col} = :1 AND {password_col} = :2"
        rows = self.execute_query(query, (username, hashed_password), fetch=True)
        return rows[0] if rows else None

    # ---------------------------
    # Hash de contraseña
    # ---------------------------
    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()
