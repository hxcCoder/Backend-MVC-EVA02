from base import BaseModel

class Cita(BaseModel):
    def __init__(self, db):
        super().__init__(db, "citas")
        self.id = None
        self.id_cliente = None
        self.id_doctor = None
        self.id_prescripcion = None
        self.fecha = None
        self.comentarios = None

    # ---------------------------
    # CREAR CITA
    # ---------------------------
    def crear_cita(self, datos: dict) -> bool:
        """
        Espera diccionario con claves:
        {'id_cliente', 'id_doctor', 'id_prescripcion', 'fecha', 'comentarios'}
        """
        return self.save(datos)

    # ---------------------------
    # LISTAR CITAS
    # ---------------------------
    def listar_citas(self):
        return self.list_all()

    # ---------------------------
    # OBTENER POR ID
    # ---------------------------
    def obtener_cita(self, cita_id: int):
        return self.get_by_id(cita_id)

    # ---------------------------
    # ELIMINAR CITA
    # ---------------------------
    def eliminar_cita(self, cita_id: int):
        return self.delete(cita_id)
