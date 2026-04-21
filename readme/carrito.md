# Equipo 4 - Módulo de Carrito

## Descripción del Módulo

Sesiones transaccionales y carrito de compras. Este módulo administra la intención de compra del cliente, el cálculo dinámico de la canasta y la retención temporal de artículos.

**Ubicación del archivo:** `routers/carrito.py`

---

## Revisión del PM

**Misión del Equipo:**
Revisar la fluidez y seguridad con la que el cliente interactúa con su orden. Es vital garantizar la confidencialidad de la información del usuario durante estas operaciones comerciales. Verificar que, al sumar o restar cantidades, el comportamiento del carrito refleje el deseo final del cliente. Remover motores de sugerencias complejas o arquitecturas de sesión de años anteriores que actualmente no aportan a la rapidez de la compra.

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

El módulo de carrito expone los siguientes endpoints bajo el prefijo `/carrito`:

- `GET /carrito/{usuario_id}` - Obtener carrito del usuario
- `POST /carrito/{usuario_id}/agregar` - Añadir producto al carrito
- `POST /carrito/{usuario_id}/quitar` - Quitar producto del carrito
- `PUT /carrito/{usuario_id}/actualizar` - Actualizar cantidad de un producto
- `GET /carrito/{usuario_id}/subtotal` - Obtener subtotal del carrito
- `DELETE /carrito/{usuario_id}` - Vaciar el carrito
- `GET /carrito/{usuario_id}/sugerencias` - Obtener sugerencias de productos

---

## Notas para el Equipo

- Presta atención a la seguridad de los datos del usuario
- Valida el comportamiento de agregar/quitar productos
- Revisa cómo se calculan los subtotales
- Asegúrate de que las cantidades se manejen correctamente
- Prueba los endpoints usando la documentación interactiva en `/docs`

