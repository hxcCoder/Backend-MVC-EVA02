# model/paciente.py
from model.base import BaseModel

class Paciente(BaseModel):
    """
    Modelo Paciente que hereda de BaseModel.
    Representa la tabla PACIENTE en la base de datos.
    """
    def __init__(self, db):
        super().__init__(db, "PACIENTE")  # Tabla en Oracle: PACIENTE

    # ---------------------------
    # Crear nuevo paciente
    # ---------------------------
    def crear_cliente(self, datos: dict) -> bool:
        return self.save(datos)

    # ---------------------------
    # Actualizar paciente
    # ---------------------------
    def actualizar_cliente(self, usuario_id: int, datos: dict) -> bool:
        query = f"""
        UPDATE {self.table} SET 
        username = :1, nombre = :2, apellido = :3, email = :4, 
        comuna = :5, fecha_primera_visita = :6
        WHERE id = :7
        """
        params = (
            datos.get("username"),
            datos.get("nombre"),
            datos.get("apellido"),
            datos.get("email"),
            datos.get("comuna"),
            datos.get("fecha_primera_visita"),
            usuario_id
        )
        result = self.execute_query(query, params)
        # Aseguramos que devuelva booleano
        return result is True

    # ---------------------------
    # Obtener paciente por ID
    # ---------------------------
    def obtener_cliente(self, usuario_id: int):
        return self.get_by_id(usuario_id)

    # ---------------------------
    # Listar todos los pacientes
    # ---------------------------
    def listar_clientes(self):
        return self.list_all()

    # ---------------------------
    # Eliminar paciente por ID
    # ---------------------------
    def eliminar_cliente(self, usuario_id: int) -> bool:
        result = self.delete(usuario_id)
        return result is True
