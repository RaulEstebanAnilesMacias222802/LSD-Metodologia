# Equipo 1 - Módulo de Usuarios

## Descripción del Módulo

Gestión de usuarios y autenticación corporativa. Este módulo es responsable del ciclo de vida de las cuentas de clientes B2B, administración de perfiles de acceso y seguridad de las sesiones en la plataforma.

**Ubicación del archivo:** `routers/usuarios.py`

---

## Revisión del PM

**Misión del Equipo:**
Evaluar el flujo de creación y mantenimiento de cuentas. Asegurar que las reglas de asignación de privilegios corporativos sean estrictas y que los formatos de contacto de los clientes cumplan con el estándar web. Adicionalmente, revisar si existen herramientas de exportación de perfiles o rutinas de conexión a bases de datos históricas que ya no sean consumidas por los clientes actuales, para simplificar la experiencia.

---

## Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Navegar al proyecto:**
   ```bash
   cd "LSD-Metodologia"
   ```

2. **Crear y activar el entorno virtual:**
   ```bash
   # En Windows
   python -m venv .venv
   .venv\Scripts\Activate
   
   # En Linux/macOS
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Iniciar el Proyecto

### Ejecutar la API

Una vez que el entorno virtual esté activado, ejecuta el siguiente comando para iniciar el servidor:

```bash
uvicorn main:app --reload
```

### Acceder a la API

- **URL Base:** `http://127.0.0.1:8000`
- **Documentación Interactiva (Swagger UI):** `http://127.0.0.1:8000/docs`
- **Documentación Alternativa (ReDoc):** `http://127.0.0.1:8000/redoc`

---

## Endpoints del Módulo

El módulo de usuarios expone los siguientes endpoints bajo el prefijo `/usuarios`:

- `POST /usuarios/registro` - Crear un nuevo usuario
- `POST /usuarios/login` - Autenticar un usuario
- `GET /usuarios/{usuario_id}` - Obtener información de un usuario
- `PUT /usuarios/{usuario_id}` - Actualizar datos del usuario
- `DELETE /usuarios/{usuario_id}` - Eliminar un usuario
- `GET /usuarios/` - Listar todos los usuarios
- `GET /usuarios/buscar/{email}` - Buscar usuario por email
- `GET /usuarios/exportar_vcard` - Exportar vCard del usuario

---

## Notas para el Equipo

- Revisa los comentarios de revisión del PM cuidadosamente
- Presta atención a la seguridad de datos sensibles
- Valida los tipos de datos y formatos esperados
- Prueba los endpoints usando la documentación interactiva en `/docs`

