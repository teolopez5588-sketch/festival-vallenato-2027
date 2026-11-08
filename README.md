# Sistema Web de Votaciones – Festival de la Leyenda Vallenata 2027

**Fundación Universitaria del Área Andina**  
**Programa:** Desarrollo Web  
**Proyecto:** Sistema Web de Votaciones  
**Tecnologías:** Python, Django, MySQL, HTML y CSS.

## 1. Descripción del proyecto

Sistema web desarrollado con Django y MySQL para gestionar ediciones, categorías, votaciones y participantes del Festival de la Leyenda Vallenata 2027.

Los usuarios pueden registrarse, iniciar sesión, consultar las categorías disponibles y emitir sus votos de manera segura.

## 2. Funcionalidades principales

- Registro e inicio de sesión.
- Administración de ediciones y categorías.
- Gestión de votaciones y participantes.
- Validación de votaciones activas y fechas.
- Un voto por usuario, categoría y edición.
- Historial individual de votos.
- Panel administrativo de Django.
- API de categorías en formato JSON.
- Almacenamiento en MySQL.

## 3. Tecnologías utilizadas

- Python 3.13.
- Django 5.2.
- MySQL 8.0.
- HTML5 y CSS3.
- mysqlclient.
- python-dotenv.

## 4. Instalación y configuración

### Clonar el repositorio

```bash
git clone https://github.com/teolopez5588-sketch/festival-vallenato-2027.git
cd festival-vallenato-2027
```

### Crear entorno virtual

```bash
python -m venv .venv
```

### Activar entorno virtual en Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Configurar variables de entorno

Crear un archivo `.env` a partir de `.env.example` y configurar las credenciales locales de MySQL. No publicar contraseñas ni claves secretas.

### Crear base de datos

```sql
CREATE DATABASE festival_vallenato;
```

### Aplicar migraciones

```bash
python manage.py migrate
```

### Crear administrador

```bash
python manage.py createsuperuser
```

### Iniciar servidor

```bash
python manage.py runserver
```

Abrir: `http://127.0.0.1:8000/`

## 5. Accesos del sistema

- Página principal: `/`
- Registro: `/registro/`
- Inicio de sesión: `/login/`
- Historial de votos: `/historial/`
- Administración: `/admin/`
- API: `/api/categorias/`

## 6. Regla de votación

Un usuario no puede registrar más de un voto en la misma categoría y edición. Puede participar en diferentes categorías.

La integridad se protege mediante validaciones en Django y una restricción única en MySQL sobre los campos usuario, categoría y edición.

## 7. API de categorías

El endpoint GET `/api/categorias/` devuelve información en formato JSON sobre las categorías activas, sus ediciones, votaciones y opciones disponibles.

## 8. Seguridad

- Autenticación de usuarios.
- Protección CSRF en formularios.
- Validación de solicitudes POST.
- Comprobación de pertenencia de las opciones a cada votación.
- Validación de fechas y estados activos.
- Restricción de votos duplicados en la base de datos.
- Variables de entorno para proteger credenciales.

## 9. Integrantes

- Mateo López Mejía.
- Sebastián De La Rosa Morelo.
- Elkin Duvan Hernandez Medina
- Maria Alejandra Mendez Quiñones.

## 10. Evidencias

Las evidencias de funcionamiento, pruebas funcionales, capturas de pantalla y demostración del sistema se presentan en el documento PDF y en el video de sustentación del proyecto.

---

**Proyecto académico – Desarrollo Web**  
**Fundación Universitaria del Área Andina – 2026**
