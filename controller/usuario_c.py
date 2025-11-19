class UsuarioController:
    def __init__(self, usuario_service):
        self.usuario_service = usuario_service#Aqui se crea el usuario_service, que es el servicio que maneja la logica de negocio.
    def crear_usuario(self, datos_usuario):
        return self.usuario_service.crear_usuario(datos_usuario)
    def obtener_usuario(self, usuario_id):
        return self.usuario_service.obtener_usuario(usuario_id)
    def actualizar_usuario(self, usuario_id, datos_usuario):
        return self.usuario_service.actualizar_usuario(usuario_id, datos_usuario)
    def eliminar_usuario(self, usuario_id):
        return self.usuario_service.eliminar_usuario(usuario_id)
    def listar_usuarios(self):
        return self.usuario_service.listar_usuarios()