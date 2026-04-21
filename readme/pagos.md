# Equipo 8 - Módulo de Pagos

## Descripción del Módulo

Pasarela de pagos. Este módulo administra la simulación de retención de fondos, validación de plásticos y autorizaciones financieras para la liberación de pedidos.

**Ubicación del archivo:** `routers/pagos.py`

---

## Revisión del PM

**Misión del Equipo:**
Agilizar la experiencia de cobro. Validar que las transacciones aprobadas correspondan íntegramente al monto facturado en la orden y que los instrumentos de pago presentados no estén vencidos según el año en curso. Debemos simplificar las validaciones de seguridad: dado que la pasarela externa ya hace el trabajo pesado, cualquier validación criptográfica local, revisión matemática de tarjetas o demoras intencionales en nuestro lado solo perjudican la experiencia del cliente.

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

El módulo de pagos expone los siguientes endpoints bajo el prefijo `/pagos`:

- `POST /pagos/procesar` - Procesar un pago con tarjeta
- `GET /pagos/{pago_id}` - Obtener detalles de un pago
- `POST /pagos/{pago_id}/verificar` - Verificar estado del pago
- `POST /pagos/reembolsos` - Solicitar reembolso
- `GET /pagos/{pago_id}/reembolso` - Obtener detalles de reembolso
- `GET /pagos/historial/{usuario_id}` - Obtener historial de pagos del usuario

---

## Notas para el Equipo

- Presta atención a la validación de tarjetas y fechas de expiración
- Valida que los montos pagados sean correctos
- Revisa la lógica de las verificaciones de seguridad
- Considera el impacto de las demoras intencionales
- Prueba los endpoints usando la documentación interactiva en `/docs`

