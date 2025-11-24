# Sistema Para Hospital – Informe

Descripcion
-

Sistema de gestion de usuarios, pacientes y doctores para un entorno clínico, 
construido en Python usando patron MVC y conexión a Oracle DB XE 21c.

El sistema se construyó manualmente, con apoyo de guías y herramientas de IA para acelerar el desarrollo.

El objetivo seria: Diseñar y construir un sistema simple, legible y funcional que permita gestionar información de un entorno clínico, 
manteniendo una arquitectura clara y una base de datos estructurada que pueda ampliarse en etapas posteriores.

El sistema permite:

- Crear, editar, listar y eliminar usuarios (Admin, Paciente, Doctor).

- Registrar pacientes y doctores.

- Autenticar usuarios con hash de contraseñas (SHA-256).

- Conectar a Oracle XE 21c para almacenar los datos de forma segura.

Herramientas y librerías utilizadas
-

Python 3.13

- Oracle DB XE 21c

- Librerías: oracledb para conexión a Oracle, hashlib para hashing de contraseñas.

# UML y relaciones

<img width="785" height="749" alt="image" src="https://github.com/user-attachments/assets/81c42ed7-1c2e-4a47-9511-bbd08c71c7e8" />



Arquitectura usada
-

Model: Clases que trabajan con Oracle (Cuenta, Paciente, Doctor).

View: Menú simple por consola para probar las funciones.

Controller: Lógica que conecta vista y modelos, representados en este caso en el main.py

Config: Conexión a la base de datos Oracle.

# Instrucciones para prueba


1. Instalar Oracle DB XE 21c y SQL Developer.

2. Ejecutar las tablas SQL provistas en Oracle.

3. Configurar config/dbconfig.py con tu usuario/password/DSN.

4. Ejecutar main.py para iniciar el menú de prueba.

5. Crear usuarios de prueba y autenticar para ver la funcionalidad.
