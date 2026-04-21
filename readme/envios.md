# Equipo 9 - Módulo de Envíos

## Descripción del Módulo

Logística y rutas de envío. Este módulo es responsable de la asignación de paqueterías, generación de guías de rastreo y cálculo de volumetría/peso para costos de distribución.

**Ubicación del archivo:** `routers/envios.py`

---

## Revisión del PM

**Misión del Equipo:**
Evaluar la correcta aplicación de nuestras políticas de entrega. Comprobar que los incentivos de envío gratuito se otorguen basados en el volumen financiero de compra del cliente, no en características físicas del paquete. Garantizar que ningún pedido pase a etapa de tránsito sin contar con información de destino válida. Retirar integraciones externas de monitoreo que no hayan sido solicitadas oficialmente o cotizadores multimoneda que no apliquen a nuestro mercado.

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

El módulo de envíos expone los siguientes endpoints bajo el prefijo `/envios`:

- `POST /envios/cotizar` - Cotizar costo de envío
- `POST /envios/crear` - Crear un envío
- `GET /envios/{envio_id}` - Obtener detalles de un envío
- `PUT /envios/{envio_id}/estado` - Actualizar estado del envío
- `GET /envios/{envio_id}/rastreo` - Obtener información de rastreo
- `GET /envios/pedido/{pedido_id}` - Obtener envíos de un pedido
- `GET /envios/costos/{codigo_postal}` - Obtener costos por código postal

---

## Notas para el Equipo

- Presta atención a la validación de direcciones
- Valida las transiciones de estado de los envíos
- Revisa cómo se calculan los costos de envío
- Asegúrate de que los criterios para envío gratis sean correctos
- Prueba los endpoints usando la documentación interactiva en `/docs`

