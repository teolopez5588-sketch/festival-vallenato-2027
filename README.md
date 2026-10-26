
@'
# Sistema Web de Votaciones
## Festival de la Leyenda Vallenata 2027

Proyecto académico desarrollado para la asignatura de Desarrollo Web de la Fundación Universitaria del Área Andina.

El sistema tiene como objetivo permitir la gestión de ediciones, categorías, votaciones y opciones participantes, así como ofrecer una interfaz web para que los usuarios registrados puedan participar en las votaciones habilitadas.

## Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **Django:** framework web basado en el patrón Modelo-Vista-Plantilla (MVT).
- **MySQL:** sistema gestor de bases de datos.
- **HTML y CSS:** estructura y presentación de la interfaz.
- **Git y GitHub:** control de versiones y alojamiento del código fuente.

## Funcionalidades implementadas

- Registro de usuarios.
- Inicio y cierre de sesión.
- Administración de ediciones, categorías, votaciones y opciones mediante Django Admin.
- Consulta de categorías y votaciones desde la base de datos.
- Registro de votos de usuarios autenticados.
- Restricción para evitar más de un voto por usuario en una misma votación.
- Validación del estado y del periodo de disponibilidad de las votaciones.
- Mensajes para informar el resultado de las operaciones.

## Requisitos

Antes de ejecutar el proyecto, se necesita:

- Python instalado.
- MySQL Server instalado y en funcionamiento.
- Git instalado.
- Una base de datos MySQL llamada `festival_vallenato`.

## Instalación y ejecución en Windows

### 1. Clonar el repositorio

```powershell
git clone https://github.com/teolopez5588-sketch/festival-vallenato-2027.git
cd festival-vallenato-2027
```

### 2. Crear y activar el entorno virtual

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si PowerShell no permite activar el entorno, se puede ejecutar Python directamente desde `.venv\Scripts\python.exe`.

### 3. Instalar las dependencias

```powershell
python -m pip install Django==5.2.18 mysqlclient==2.3.0 python-dotenv
```

### 4. Configurar las variables de entorno

Crear un archivo llamado `.env` en la carpeta principal del proyecto. Este archivo debe contener las variables que utiliza `config/settings.py`.

Ejemplo de configuración local:

```dotenv
DJANGO_SECRET_KEY=REEMPLAZAR_POR_UNA_CLAVE_SEGURA
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=festival_vallenato
DB_USER=root
DB_PASSWORD=TU_CLAVE_LOCAL_DE_MYSQL
DB_HOST=127.0.0.1
DB_PORT=3307
```

Los valores deben coincidir con la configuración del servidor MySQL y con las variables leídas por el proyecto. La clave secreta y la contraseña son ejemplos de configuración: cada instalación debe utilizar sus propios valores.

**Importante:** no publicar el archivo `.env` ni compartir credenciales reales.

### 5. Crear la base de datos

Desde MySQL, crear una base de datos con el nombre configurado:

```sql
CREATE DATABASE festival_vallenato
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

El usuario configurado debe tener permisos para acceder a esa base de datos.

### 6. Aplicar las migraciones

Desde la carpeta del proyecto, ejecutar:

```powershell
python manage.py migrate
```

### 7. Crear un usuario administrador

```powershell
python manage.py createsuperuser
```

Seguir las instrucciones de la terminal para crear las credenciales del administrador.

### 8. Iniciar el servidor de desarrollo

```powershell
python manage.py runserver
```

Abrir en el navegador:

- **Aplicación:** http://127.0.0.1:8000/
- **Administración:** http://127.0.0.1:8000/admin/

El servidor de desarrollo está destinado a pruebas locales, no a producción.

## Estructura del proyecto

```text
festival-vallenato-2027/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── votaciones/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── .gitignore
├── manage.py
└── README.md
```

## Integrantes del equipo

- Mateo López Mejía
- Elkin Hernandez
- Alejandra
- Sebastián De La Rosa Morelo

## Repositorio

Código fuente del proyecto:

https://github.com/teolopez5588-sketch/festival-vallenato-2027

## Alcance académico

Este proyecto corresponde a una implementación académica en desarrollo. La ejecución en otro equipo requiere configurar las dependencias, las variables de entorno y la base de datos. La publicación del código en GitHub no implica que la aplicación esté desplegada en un servidor público.

---
Fundación Universitaria del Área Andina  
Asignatura: Desarrollo Web  
Proyecto: Sistema Web de Votaciones – Festival de la Leyenda Vallenata 2027
'@ | Set-Content -Path README.md -Encoding utf8
