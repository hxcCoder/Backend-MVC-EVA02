# model/base.py
from typing import Any, Dict, Tuple, List

class BaseModel:

    def __init__(self, db, table: str, pk: str = "id"):
        self.db = db
        self.table = table
        self.pk = pk  # ahora configurable (id, usuario_id, etc.)

    # ---------------------------
    # Ejecutar query SQL
    # ---------------------------
    def execute_query(self, query: str, params: Tuple = (), fetch: bool = False, as_dict: bool = False):
        if not self.db.connection:
            self.db.conectar()

        cursor = self.db.obtener_cursor()
        cursor.execute(query, params)

        if fetch:
            rows = cursor.fetchall()
            if not rows:
                return []

            if as_dict:
                cols = [c[0] for c in cursor.description]
                return [dict(zip(cols, row)) for row in rows]

            return rows

        self.db.connection.commit()
        return []

    # ---------------------------
    # Insertar registro
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
            self.db.connection.rollback()
            return False

    # ---------------------------
    # Buscar por PK
    # ---------------------------
    def get_by_id(self, record_id: int, as_dict=True):
        query = f"SELECT * FROM {self.table} WHERE {self.pk} = :1"
        result = self.execute_query(query, (record_id,), fetch=True, as_dict=as_dict)
        return result[0] if result else None

    # ---------------------------
    # Listar todo
    # ---------------------------
    def list_all(self, as_dict=True) -> List[Dict[str, Any]]:
        query = f"SELECT * FROM {self.table}"
        return self.execute_query(query, fetch=True, as_dict=as_dict)

    # ---------------------------
    # Eliminar por PK
    # ---------------------------
    def delete(self, record_id: int) -> bool:
        try:
            query = f"DELETE FROM {self.table} WHERE {self.pk} = :1"
            self.execute_query(query, (record_id,))
            return True
        except Exception as e:
            print("Error al eliminar:", e)
            self.db.connection.rollback()
            return False
