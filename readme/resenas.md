# Equipo 9 - Módulo de Reseñas

## Descripción del Módulo

Auditoría de reseñas y reportes gerenciales. Este módulo recopila la retroalimentación del cliente sobre el catálogo y genera inteligencia de negocios y reportes de ventas para directivos.

**Ubicación del archivo:** `routers/resenas.py`

---

## Revisión del PM

**Misión del Equipo:**
Analizar la veracidad de la opinión en el catálogo. Asegurar que la calificación global de cada artículo refleje con precisión matemática el promedio real y proteger el sistema contra la manipulación de puntajes (spam de un mismo cliente). En la sección gerencial, asegurar que los listados de ventas destaquen verdaderamente a los productos estrella del momento. Limpiar el módulo de motores de análisis complejos o formatos de reporte antiguos que el dashboard actual no soporta.

---

## Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Navegar al proyecto:**
   ```bash
   cd "LSD-Actividad"
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

El módulo de reseñas expone los siguientes endpoints bajo el prefijo `/resenas`:

- `POST /resenas/crear` - Crear una nueva reseña para un producto
- `GET /resenas/producto/{producto_id}` - Obtener reseñas de un producto
- `GET /resenas/producto/{producto_id}/promedio` - Obtener calificación promedio
- `PUT /resenas/{resena_id}` - Actualizar una reseña
- `DELETE /resenas/{resena_id}` - Eliminar una reseña
- `POST /resenas/{resena_id}/upvote` - Dar voto positivo a una reseña
- `POST /resenas/{resena_id}/downvote` - Dar voto negativo a una reseña
- `GET /resenas/reportes/mas_vendidos` - Obtener reporte de productos más vendidos

---

## Notas para el Equipo

- Presta atención al cálculo correcto del promedio de calificaciones
- Valida que un usuario no pueda dejar múltiples reseñas del mismo producto
- Revisa el orden de los reportes de ventas
- Asegúrate de que se limpien datos inválidos
- Prueba los endpoints usando la documentación interactiva en `/docs`

