# Equipo 6 - Módulo de Promociones

## Descripción del Módulo

Motor de promociones y reglas de negocio. Este módulo verifica la aplicabilidad de campañas de descuento, vigencias del calendario comercial y restricciones de canje por usuario.

**Ubicación del archivo:** `routers/promociones.py`

---

## Revisión del PM

**Misión del Equipo:**
Asegurar que el sistema respete estrictamente los tiempos reales de las campañas y evite la aplicación prematura de descuentos. Validar la política de fidelidad: los cupones especiales de bienvenida deben ser beneficios de un solo uso por cliente. Asegurar que las promociones más agresivas no resulten en escenarios de cobro financiero inviables. Limpiar el código de programas de lealtad rechazados o generadores masivos no utilizados.

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

El módulo de promociones expone los siguientes endpoints bajo el prefijo `/promociones`:

- `GET /promociones/cupones` - Listar todos los cupones
- `GET /promociones/cupones/activos` - Listar cupones activos
- `GET /promociones/cupones/vigentes` - Listar cupones vigentes
- `POST /promociones/validar_cupon/{codigo}` - Validar un cupón
- `POST /promociones/aplicar_descuento` - Aplicar descuento a un total
- `GET /promociones/puntos/{usuario_id}` - Obtener puntos de lealtad
- `POST /promociones/canjear_puntos` - Canjear puntos por descuento

---

## Notas para el Equipo

- Presta atención a la validación de fechas de vigencia
- Valida el comportamiento de cupones con restricciones
- Asegúrate de que los descuentos no generen valores negativos
- Revisa la lógica de uno vs. múltiples usos de cupones
- Prueba los endpoints usando la documentación interactiva en `/docs`

