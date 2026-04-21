# Equipo 3 - Módulo de Inventario

## Descripción del Módulo

Control de inventario y almacenes. Este módulo es responsable de la conciliación de existencias físicas, apartados temporales durante la compra y disparadores de alertas de reabastecimiento logístico.

**Ubicación del archivo:** `routers/inventario.py`

---

## Revisión del PM

**Misión del Equipo:**
Garantizar que las políticas de stock del sistema reflejen la realidad del almacén: no podemos permitir apartados de mercancía que no existe físicamente. Auditar los niveles de alerta para asegurar que los avisos de reabastecimiento se emitan en el umbral exacto acordado por gerencia. Por último, desconectar integraciones con modelos de análisis predictivo o bases de proveedores antiguos que estén pausando o frenando el proceso de actualización.

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

El módulo de inventario expone los siguientes endpoints bajo el prefijo `/inventario`:

- `GET /inventario/productos` - Obtener nivel de stock de todos los productos
- `GET /inventario/productos/{producto_id}` - Obtener stock de un producto específico
- `PUT /inventario/actualizar/{producto_id}` - Actualizar stock de un producto
- `POST /inventario/reservar/{producto_id}` - Reservar cantidad de stock
- `POST /inventario/liberar/{producto_id}` - Liberar stock reservado
- `GET /inventario/alertas` - Obtener alertas de bajo stock
- `GET /inventario/prediccion_demanda_ia` - Predicción de demanda

---

## Notas para el Equipo

- Presta atención a la consistencia de los datos de stock
- Valida que no se permitan valores negativos
- Revisa los umbrales de alerta configurados
- Considera el impacto de las operaciones de reserva
- Prueba los endpoints usando la documentación interactiva en `/docs`

