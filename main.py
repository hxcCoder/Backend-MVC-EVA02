from model.services.login_service  import LoginService
from controller.login_c import LoginController
from view.view import mostrar_menu
import oracledb

# Conexión a Oracle
db = oracledb.connect(user="system", password="oracle", dsn="localhost/XE")

login_service = LoginService(db)
login_controller = LoginController(login_service)

username = input("Usuario: ")
password = input("Contraseña: ")

usuario = login_controller.login(username, password)

if usuario:
    print("Login exitoso!")
    mostrar_menu(usuario)
else:
    print("Usuario o contraseña incorrectos")
