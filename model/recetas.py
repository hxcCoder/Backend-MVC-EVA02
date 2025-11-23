class Receta:
    def __init__(self, db):
        self.db = db

    def crear(self, id_paciente, id_medico, descripcion):
        cursor = self.db.obtener_cursor()
        cursor.execute("""
            INSERT INTO recetas (id_paciente, id_medico, descripcion)
            VALUES (:1, :2, :3)
        """, (id_paciente, id_medico, descripcion))
        self.db.connection.commit()
        return True

    def listar(self):
        cursor = self.db.obtener_cursor()
        cursor.execute("SELECT * FROM recetas")
        return [dict(zip([c[0] for c in cursor.description], fila)) for fila in cursor]

    def obtener_por_id(self, id_):
        cursor = self.db.obtener_cursor()
        cursor.execute("SELECT * FROM recetas WHERE id = :1", (id_,))
        fila = cursor.fetchone()
        return dict(zip([c[0] for c in cursor.description], fila)) if fila else None

    def eliminar(self, id_):
        cursor = self.db.obtener_cursor()
        cursor.execute("DELETE FROM recetas WHERE id = :1", (id_,))
        self.db.connection.commit()
        return True
