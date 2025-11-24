class Agenda:
    def __init__(self, db):
        self.db = db
        self.table = "agenda"

    # ---------------------------
    # Crear agenda
    # ---------------------------
    def crear(self, id_paciente, id_medico, fecha_consulta, estado):
        try:
            cursor = self.db.obtener_cursor()
            cursor.execute(f"""
                INSERT INTO {self.table} (id_paciente, id_medico, fecha_consulta, estado)
                VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4)
            """, (id_paciente, id_medico, fecha_consulta, estado))

            self.db.connection.commit()
            return True
        except Exception as e:
            print("Error al crear agenda:", e)
            self.db.connection.rollback()
            return False

    # ---------------------------
    # Listar todas
    # ---------------------------
    def listar(self):
        cursor = self.db.obtener_cursor()
        cursor.execute(f"SELECT * FROM {self.table}")
        columnas = [c[0] for c in cursor.description]
        return [dict(zip(columnas, fila)) for fila in cursor]

    # ---------------------------
    # Obtener por ID
    # ---------------------------
    def obtener_por_id(self, id_):
        cursor = self.db.obtener_cursor()
        cursor.execute(f"SELECT * FROM {self.table} WHERE id = :1", (id_,))
        fila = cursor.fetchone()
        return dict(zip([c[0] for c in cursor.description], fila)) if fila else None

    # ---------------------------
    # Actualizar agenda
    # ---------------------------
    def actualizar(self, id_, datos):
        try:
            cursor = self.db.obtener_cursor()
            cursor.execute(f"""
                UPDATE {self.table}
                SET id_paciente = :1,
                    id_medico   = :2,
                    fecha_consulta = TO_DATE(:3, 'YYYY-MM-DD'),
                    estado      = :4
                WHERE id = :5
            """, (
                datos["id_paciente"],
                datos["id_medico"],
                datos["fecha_consulta"],
                datos["estado"],
                id_
            ))
            self.db.connection.commit()
            return True
        except Exception as e:
            print("Error al actualizar agenda:", e)
            self.db.connection.rollback()
            return False

    # ---------------------------
    # Eliminar
    # ---------------------------
    def eliminar(self, id_):
        try:
            cursor = self.db.obtener_cursor()
            cursor.execute(f"DELETE FROM {self.table} WHERE id = :1", (id_,))
            self.db.connection.commit()
            return True
        except Exception as e:
            print("Error al eliminar agenda:", e)
            self.db.connection.rollback()
            return False
