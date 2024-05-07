![](https://github.com/RominaPrestupa/Alkemy_ProyectoFinal/blob/master/static/imagenes/alk1.png)
# IT Bootcamp POO Python 

### Trabajo integrador: Sistema de Gestión de personas
### *Fundamentos de Django*
<br>

### Presentación

Bienvenido/a a mi proyecto final! 
Este trabajo se enmarcó en la edición 2024 del bootcamp de POO Python.

El proyecto que vas a encontrar acá es el resultado final de 10 intensas semanas de cursada.  Si bien comencé ya teniendo un background en lógica de programación y Python orientado a la Ciencia de Datos, en este bootcamp logré adquirir nociones fundamentales sobre programación orientada a objetos, Django, Jinja, SQLite3, entre otras. 

El proyecto consiste en un sistema de gestión que permite llevar un registro completo de proveedores y productos,  desarrollado integramente en Python 3.11.0, con el framework Django 5.0.4. Proporciona funcionalidades CRUD (*Crear, Leer, Actualizar, Eliminar*) para productos y proveedores, así como la autenticación de usuarios y/o gestión de permisos.
<br><br>

### Características

- **Autenticación de Usuarios**: Permite a los usuarios registrarse, iniciar sesión y cerrar sesión en el sistema;
- **Gestión de Permisos**: Basado en roles, el sistema asigna diferentes permisos a los usuarios según su rol;
- **CRUD de Productos y Proveedores**: Permite a los usuarios autorizados crear, leer, actualizar y eliminar productos y proveedores (*para los fines del proyecto, solo se incluye Create y Read*);
- **Listado de Productos y Proveedores**: Proporciona una lista detallada de todos los productos y proveedores existentes en el sistema;
- **Diseño responsive**: se incorporó el uso de la librería Bootstrap para una experiencia de usuario optimizada en dispositivos móviles y de escritorio.
<br><br>
### Instalación y uso

                
1. Cloná este repositorio en tu máquina local
2. Instalá las dependencias del proyecto utilizando pip:

`pip install -r requirements.txt`

3. Ejecutá las migraciones de Django para crear la base de datos:
   
`python manage.py migrate`

4. Crea un superusuario ejecutando `python manage.py createsuperuser` y sigue las instrucciones para completar la información del usuario.

5. Iniciá el servidor de desarrollo:

`python manage.py runserver`

6. Accedé a la aplicación en tu navegador web en la dirección http://localhost:8000.
   
7. Ingresá con las credenciales del superusario que creaste en el paso 4 y explorá las funcionalidades del sistema.

8. Agregá, consultá, editá o eliminá productos y proveedores existentes para una rápida referencia.
<br><br>

----               

### Tecnologías utilizadas

                
- Python
- Django
- Bootstrap (para el diseño responsive)
