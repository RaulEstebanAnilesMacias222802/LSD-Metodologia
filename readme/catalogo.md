# Equipo 2 - Módulo de Catálogo

## Descripción del Módulo

Gestión del catálogo de productos y búsqueda avanzada. Este módulo gestiona el inventario público, la exposición de atributos técnicos de productos y los motores de filtrado para la vitrina del cliente.

**Ubicación del archivo:** `routers/catalogo.py`

---

## Revisión del PM

**Misión del Equipo:**
Analizar la experiencia de búsqueda del cliente. Necesitamos que los límites de precio en los filtros abarquen exactamente el presupuesto del cliente. Validar cómo se comporta la vitrina cuando un cliente navega por listados sin contenido. Identificar y remover procesos paralelos de análisis de datos o generación de metadatos que estén ejecutándose en el servidor pero que el portal web frontal no esté utilizando actualmente.

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

El módulo de catálogo expone los siguientes endpoints bajo el prefijo `/catalogo`:

- `GET /catalogo/productos` - Listar todos los productos
- `GET /catalogo/productos/{producto_id}` - Obtener detalles de un producto
- `GET /catalogo/buscar` - Buscar productos
- `GET /catalogo/search/{query}` - Búsqueda alternativa de productos
- `GET /catalogo/filtrar` - Filtrar productos por categoría, precio, etc.
- `GET /catalogo/categorias` - Listar categorías disponibles

---

## Notas para el Equipo

- Presta atención a la duplicación de funcionalidades
- Revisa los filtros de precio y cómo se comportan con casos límite
- Considera el rendimiento del servidor con operaciones de búsqueda
- Prueba los endpoints usando la documentación interactiva en `/docs`

