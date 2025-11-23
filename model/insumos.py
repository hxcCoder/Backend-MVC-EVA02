class Insumo:
    def __init__(self, db):
        self.db = db

    def crear(self, nombre, tipo, stock):
        cursor = self.db.obtener_cursor()
        cursor.execute("""
            INSERT INTO insumos (nombre, tipo, stock)
            VALUES (:1, :2, :3)
        """, (nombre, tipo, stock))
        self.db.connection.commit()
        return True

    def listar(self):
        cursor = self.db.obtener_cursor()
        cursor.execute("SELECT * FROM insumos")
        return [dict(zip([c[0] for c in cursor.description], fila)) for fila in cursor]

    def obtener_por_id(self, id_):
        cursor = self.db.obtener_cursor()
        cursor.execute("SELECT * FROM insumos WHERE id = :1", (id_,))
        fila = cursor.fetchone()
        return dict(zip([c[0] for c in cursor.description], fila)) if fila else None

    def actualizar(self, id_, datos):
        cursor = self.db.obtener_cursor()
        cursor.execute("""
            UPDATE insumos SET nombre=:1, tipo=:2, stock=:3
            WHERE id=:4
        """, (datos["nombre"], datos["tipo"], datos["stock"], id_))
        self.db.connection.commit()
        return True

    def eliminar(self, id_):
        cursor = self.db.obtener_cursor()
        cursor.execute("DELETE FROM insumos WHERE id = :1", (id_,))
        self.db.connection.commit()
        return True
