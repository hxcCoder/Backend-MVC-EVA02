# EVA_02 // Backend-Hospital

Sistema Para Hospital – Informe

1. Descripción 

Es un sistema de gestion de usuarios para un hospital de ejemplo, Sistema de gestion de usuarios, pacientes y doctores para un entorno clínico, construido en Python usando patron MVC y conexión a Oracle DB XE 21c.
Fue hecho a mano usando guias y herramientas como la IA, esta funcional y organice los datos para que se puedan entender facilmente.

Se puede: Crear, actualizar, listar y eliminar cuentas de usuarios (Admin, Paciente, Doctor).

Autenticacion segura con hash de contraseñas.

Gestión de pacientes y doctores mediante modelos especificos.

2. Herramientas y librerías utilizadas

Python 3.13

Oracle DB XE 21c

Librerías: oracledb para conexión a Oracle, hashlib para hashing de contraseñas.

# UML y relaciones

Clases: Cuenta → Cliente/Doctor, Paciente, Cita, BaseModel.

Patrón MVC:

Model: manejo de datos y DB.

View: menú y presentación.

Controller/Main: lógica de interacción.

-
# Instrucciones para prueba

-

Instalar Oracle DB XE 21c y SQL Developer.

Ejecutar las tablas SQL provistas en Oracle.

Configurar config/dbconfig.py con tu usuario/password/DSN.

Ejecutar main.py para iniciar el menú de prueba.

Crear usuarios de prueba y autenticar para ver la funcionalidad.
