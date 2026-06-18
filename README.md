# Proyecto_POO_ValidacionCorreo - Grupo 5
## Autores
- Karen Alvarez Yagual
- Andres Macias Villamar
- Emily Pino Loor
- Alexis Rodriguez Crespin
- Sofia Vasquez Chila

## Descripción

Aplicación desarrollada en Python utilizando PySide6 y Programación Orientada a Objetos.

El sistema permite registrar usuarios mediante los siguientes datos:

* Código
* Nombre
* Fecha
* Correo electrónico

Los registros se muestran en una tabla y se almacenan en un archivo de texto.

## Funcionalidades

* Registro de usuarios.
* Validación de campos vacíos.
* Validación de código numérico de 5 dígitos.
* Validación de nombre (solo letras).
* Validación de correo electrónico mediante expresiones regulares.
* Visualización de registros en una tabla.
* Eliminación de registros seleccionados.
* Almacenamiento permanente en archivo de texto.

## Validación de Correo

La validación del correo electrónico se realiza utilizando expresiones regulares (Regex).

Ejemplos válidos:

* [usuario@gmail.com](mailto:usuario@gmail.com)
* [nombre.apellido@hotmail.com](mailto:nombre.apellido@hotmail.com)
* [estudiante2026@instituto.edu.ec](mailto:estudiante2026@instituto.edu.ec)

Ejemplos inválidos:

* usuario@
* @gmail.com
* usuario gmail.com
* correo.com

## Tecnologías utilizadas

* Python
* PySide6
* Qt Designer




Emily
