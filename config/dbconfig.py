import oracledb
import os

class ConexionOracle:
    def __init__(self, user=None, password=None, dsn=None):#Aqui defino sus funciones
        self.user = user or os.getenv("DB_USER", "clinica")#El user de ejemplo
        self.password = password or os.getenv("DB_PASS", "mi_pass_seguro")#aqui esta la contraseña
        self.dsn = dsn or os.getenv("DB_DSN", "localhost:1521/XEPDB1")#Y esto el dns para la conexion
        self.conn = None#Conexion vacia

    def conectar(self):#Conectar a la base de datos
        if self.conn:
            return self.conn
        try:
            self.conn = oracledb.connect(self.user, self.password, self.dsn)
            return self.conn
        except oracledb.DatabaseError as e:
            # log y re-lanzar o manejar
            raise

    def obtener_cursor(self):
        if not self.conn:
            self.conectar()
        return self.conn.cursor()

    def cerrar(self):
        if self.conn:
            self.conn.close()
            self.conn = None
