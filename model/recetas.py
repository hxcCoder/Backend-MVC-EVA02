class Receta:
    def __init__(self, db):
        self.db = db

    # =============================
    # CREATE
    # =============================
    def crear(self, id_paciente, id_medico, descripcion):
        try:
            cursor = self.db.obtener_cursor()
            cursor.execute("""
                INSERT INTO recetas (id_paciente, id_medico, descripcion)
                VALUES (:1, :2, :3)
            """, (id_paciente, id_medico, descripcion))
            self.db.connection.commit()
            return True
        except Exception as e:
            print("Error al crear receta:", e)
            return False

    # =============================
    # READ
    # =============================
    def listar(self):
        cursor = self.db.obtener_cursor()
        cursor.execute("SELECT * FROM recetas")
        return [dict(zip([c[0] for c in cursor.description], fila)) for fila in cursor]

    def obtener_por_id(self, id_):
        cursor = self.db.obtener_cursor()
        cursor.execute("SELECT * FROM recetas WHERE id = :1", (id_,))
        fila = cursor.fetchone()
        return dict(zip([c[0] for c in cursor.description], fila)) if fila else None

    # =============================
    # UPDATE
    # =============================
    def actualizar(self, id_, nueva_desc):
        try:
            cursor = self.db.obtener_cursor()
            cursor.execute("""
                UPDATE recetas 
                SET descripcion = :1 
                WHERE id = :2
            """, (nueva_desc, id_))
            self.db.connection.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print("Error al actualizar receta:", e)
            return False

    # =============================
    # DELETE
    # =============================
    def eliminar(self, id_):
        try:
            cursor = self.db.obtener_cursor()
            cursor.execute("DELETE FROM recetas WHERE id = :1", (id_,))
            self.db.connection.commit()
            return True
        except Exception as e:
            print("Error al eliminar receta:", e)
            return False
