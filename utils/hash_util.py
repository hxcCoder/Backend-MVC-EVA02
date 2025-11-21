import hashlib

class HashUtil:
    @staticmethod
    def hash_password(password: str) -> str:
        """
        Genera un hash seguro de la contraseña usando SHA-256.
        """
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    @staticmethod
    def verify_password(password: str, hashed: str) -> bool:
        """
        Verifica si la contraseña coincide con el hash guardado.
        """
        return hashlib.sha256(password.encode("utf-8")).hexdigest() == hashed
