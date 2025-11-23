class Agenda:
    def __init__(self, db):
        self.db = db

    def crear(self, id_paciente, id_medico, fecha_consulta, estado):
        cursor = self.db.obtener_cursor()
        cursor.execute("""
            INSERT INTO agenda (id_paciente, id_medico, fecha_consulta, estado)
            VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4)
        """, (id_paciente, id_medico, fecha_consulta, estado))
        self.db.connection.commit()
        return True

    def listar(self):
        cursor = self.db.obtener_cursor()
        cursor.execute("SELECT * FROM agenda")
        return [dict(zip([c[0] for c in cursor.description], fila)) for fila in cursor]
