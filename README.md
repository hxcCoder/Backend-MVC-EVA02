# Sistema Para Hospital – Informe

Descripcion
-

Sistema de gestion de usuarios, pacientes y doctores para un entorno clínico, 
construido en Python usando patron MVC y conexión a Oracle DB XE 21c.

Fue hecho a mano usando guias y herramientas como la IA, esta funcional y organice los datos para que se puedan entender facilmente.

Se puede: Crear, actualizar, listar y eliminar cuentas de usuarios (Admin, Paciente, Doctor).

- Autenticacion segura con hash de contraseñas.

- Gestión de pacientes y doctores mediante modelos especificos.

- Herramientas y librerías utilizadas
Python 3.13

- Oracle DB XE 21c

- Librerías: oracledb para conexión a Oracle, hashlib para hashing de contraseñas.

# UML y relaciones

<img width="787" height="739" alt="image" src="https://github.com/user-attachments/assets/e211bacc-fa5e-48a3-a4ef-e10d8bb1211d" />

- Clases: Cuenta → Cliente/Doctor, Paciente, Cita, BaseModel.

- Patrón MVC:

- Model: manejo de datos y DB.

- View: menú y presentación.

- Controller/Main: lógica de interacción.

# Instrucciones para prueba


1. Instalar Oracle DB XE 21c y SQL Developer.

2. Ejecutar las tablas SQL provistas en Oracle.

3. Configurar config/dbconfig.py con tu usuario/password/DSN.

4. Ejecutar main.py para iniciar el menú de prueba.

5. Crear usuarios de prueba y autenticar para ver la funcionalidad.
