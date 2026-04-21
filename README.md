# 🚀 Punto de Inicio - LSD-Actividad

¡Bienvenido! Este archivo te guiará sobre cómo comenzar con tu parte del proyecto.

---

## ¿Cuál es mi equipo?

Cada equipo es responsable de un módulo específico dentro de la plataforma Amazonas. Consulta la tabla a continuación para identificar tu equipo y rama correspondiente:

| Equipo | Módulo | Rama GitHub | README |
|--------|--------|-------------|--------|
| **Equipo 1** | Usuarios | `equipo-1-usuarios` | [usuarios.md](readme/usuarios.md) |
| **Equipo 2** | Catálogo | `equipo-2-catalogo` | [catalogo.md](readme/catalogo.md) |
| **Equipo 3** | Inventario | `equipo-3-inventario` | [inventario.md](readme/inventario.md) |
| **Equipo 4** | Carrito | `equipo-4-carrito` | [carrito.md](readme/carrito.md) |
| **Equipo 5** | Pedidos | `equipo-5-pedidos` | [pedidos.md](readme/pedidos.md) |
| **Equipo 6** | Promociones | `equipo-6-promociones` | [promociones.md](readme/promociones.md) |
| **Equipo 7** | Pagos | `equipo-7-pagos` | [pagos.md](readme/pagos.md) |
| **Equipo 8** | Envíos | `equipo-8-envios` | [envios.md](readme/envios.md) |
| **Equipo 9** | Reseñas | `equipo-9-resenas` | [resenas.md](readme/resenas.md) |

---

## 📋 Pasos para Comenzar

### 1️⃣ Clonar el Repositorio (si aún no lo has hecho)

```bash
git clone https://github.com/tu-usuario/LSD-Actividad.git
cd LSD-Actividad
```

### 2️⃣ Cambiar a tu Rama de Equipo

Reemplaza `equipo-X-modulo` con tu rama correspondiente:

**Ejemplo para Equipo 1 (Usuarios):**
```bash
git checkout equipo-1-usuarios
```

### 3️⃣ Leer las Indicaciones de tu Módulo

Una vez en tu rama, abre el archivo README correspondiente a tu módulo en la carpeta `readme/`:

- **Equipo 1:** Lee [readme/usuarios.md](readme/usuarios.md)
- **Equipo 2:** Lee [readme/catalogo.md](readme/catalogo.md)
- **Equipo 3:** Lee [readme/inventario.md](readme/inventario.md)
- **Equipo 4:** Lee [readme/carrito.md](readme/carrito.md)
- **Equipo 5:** Lee [readme/pedidos.md](readme/pedidos.md)
- **Equipo 6:** Lee [readme/promociones.md](readme/promociones.md)
- **Equipo 7:** Lee [readme/pagos.md](readme/pagos.md)
- **Equipo 8:** Lee [readme/envios.md](readme/envios.md)
- **Equipo 9:** Lee [readme/resenas.md](readme/resenas.md)

### 4️⃣ Instalar y Ejecutar el Proyecto

En el README de tu módulo encontrarás instrucciones detalladas para:

1. **Instalar dependencias** - Cómo configurar tu entorno virtual
2. **Iniciar el servidor** - Cómo ejecutar la API
3. **Acceder a la documentación** - Cómo probar los endpoints

### 5️⃣ Identificar y Resolver los Bugs

En el README de tu módulo hay una sección llamada **"Revisión del PM"** que lista los problemas que debes encontrar y resolver.

---

## 📁 Estructura del Proyecto

```
LSD-Actividad/
├── main.py                    # Archivo principal de FastAPI
├── requirements.txt           # Dependencias del proyecto
├── README.md                  # Documentación general (oculta info de bugs)
├── INICIO.md                  # Este archivo
├── routers/                   # Módulos de la aplicación
│   ├── usuarios.py
│   ├── catalogo.py
│   ├── inventario.py
│   ├── carrito.py
│   ├── pedidos.py
│   ├── promociones.py
│   ├── pagos.py
│   ├── envios.py
│   └── resenas.py
└── readme/                    # README específicos por módulo
    ├── usuarios.md
    ├── catalogo.md
    ├── inventario.md
    ├── carrito.md
    ├── pedidos.md
    ├── promociones.md
    ├── pagos.md
    ├── envios.md
    └── resenas.md
```

---

## 🛠️ Requisitos Técnicos

- **Python 3.8 o superior**
- **pip** (gestor de paquetes)
- **Git** (para clonar y cambiar de rama)

---

## 💡 Consejos Útiles

**Lee tu README completo** - Contiene información crucial sobre tu módulo  
**Usa la documentación interactiva** - Accede a `http://127.0.0.1:8000/docs` para probar endpoints  
**Trabaja con tu equipo** - Comunica tus hallazgos y colabora en las soluciones  
**Haz commits regulares** - Guarda tu progreso en la rama de tu equipo  

---

## ❓ Preguntas Frecuentes

**¿Puedo ver el código de otros equipos?**  
Sí, puedes ver los archivos en las ramas de otros equipos, pero tu enfoque principal debe ser resolver los problemas de tu propio módulo.

**¿Qué sucede si encuentro un bug en otro módulo?**  
Reporta el hallazgo, pero mantén tu trabajo enfocado en tu módulo asignado.

**¿Debo instalar las dependencias cada vez que cambio de rama?**  
No necesariamente, pero es recomendable ejecutar `pip install -r requirements.txt` para asegurar que todo está correctamente instalado.

---

## ✨ ¡Buen Trabajo!

Ahora que sabes cómo comenzar, dirígete a tu rama de equipo y sigue las indicaciones en el README de tu módulo.

**¿Listo? ¡Vamos!** 🚀

