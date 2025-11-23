import oracledb

class ConexionOracle:
    def __init__(self, user="System", password="Ina.2025", dsn="localhost/xe"):
        self.user = user
        self.password = password
        self.dsn = dsn
        self.connection = None

    def conectar(self):
        try:
            self.connection = oracledb.connect(
                user=self.user,
                password=self.password,
                dsn=self.dsn
            )
            print("Conexión exitosa a Oracle")
        except Exception as e:
            print(f"[ERROR] Conexión a Oracle: {e}")

    def obtener_cursor(self):
        if self.connection:
            return self.connection.cursor()
        else:
            raise Exception("No hay conexión a la base de datos")
