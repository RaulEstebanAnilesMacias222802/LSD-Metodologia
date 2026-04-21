# Equipo 5 - Módulo de Pedidos

## Descripción del Módulo

Procesamiento de pedidos e impuestos. Este módulo transforma la intención de compra del carrito en una orden en firme, aplicando marcos fiscales y consolidando el inicio de la logística.

**Ubicación del archivo:** `routers/pedidos.py`

---

## Revisión del PM

**Misión del Equipo:**
Auditar la transición del carrito al pedido formal. Asegurar que las transiciones de estado de las órdenes sigan un flujo comercial lógico (evitando saltos operativos no autorizados). Es crítico validar con el área contable que el cálculo de impuestos se aplique únicamente sobre los rubros legales correctos. Simplificar el módulo retirando formatos de facturación obsoletos o métodos de cotización alternativos que ya no se ofrezcan.

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

El módulo de pedidos expone los siguientes endpoints bajo el prefijo `/pedidos`:

- `POST /pedidos/crear` - Crear un nuevo pedido desde el carrito
- `GET /pedidos/{pedido_id}` - Obtener detalles de un pedido
- `GET /pedidos/usuario/{usuario_id}` - Listar pedidos de un usuario
- `PUT /pedidos/{pedido_id}/estado` - Actualizar estado del pedido
- `GET /pedidos/{pedido_id}/factura` - Obtener factura del pedido
- `GET /pedidos/{pedido_id}/iva` - Obtener detalles de IVA
- `POST /pedidos/simular_cripto` - Simular cotización en criptomoneda

---

## Notas para el Equipo

- Presta atención al cálculo correcto del IVA
- Valida las transiciones de estado de los pedidos
- Asegúrate de que el carrito se vacíe correctamente
- Revisa el manejo de los datos fiscales
- Prueba los endpoints usando la documentación interactiva en `/docs`

