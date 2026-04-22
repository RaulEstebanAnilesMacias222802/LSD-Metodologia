# LSD-Metodologia

El objetivo de la actividad es identificar y eliminar desperdicios así como reparar bugs. En cada uno de los módulos se encuentra la descripción general de cómo debe funcionar el módulo, así como realizar las indicaciones del project manager (*PM*) para la auditoría del módulo asignado (*TO-DO / Misión del Equipo*).

Registro de métricas por equipo en google sheets: [Enlace](https://docs.google.com/spreadsheets/d/19jsudENN9si2xRXA2xMRey_ENPdcLJGKedNo_68VFOE/edit?usp=sharing)

Nota: En el marco de LSD, un desperdicio es cualquier elemento, proceso o código que no aporta valor al usuario final y añade complejidad al mantenimiento.

---

## ¿Cuál es mi equipo?

Cada equipo es responsable de un módulo específico dentro de la plataforma "*Amazonas*". Consulta la tabla a continuación para identificar tu equipo y rama correspondiente:

| Equipo | Integrante | Módulo | Rama GitHub | README |
|--------|------------|--------|-------------|--------|
| **Equipo 1** | **Jesus Alejandro** | Usuarios | `equipo-1-usuarios` | [usuarios.md](readme/usuarios.md) |
| **Equipo 2** | **Jennifer** | Catálogo | `equipo-2-catalogo` | [catalogo.md](readme/catalogo.md) |
| **Equipo 3** | **Jesus Andre** | Inventario | `equipo-3-inventario` | [inventario.md](readme/inventario.md) |
| **Equipo 4** | **Alan Alejandro** | Carrito | `equipo-4-carrito` | [carrito.md](readme/carrito.md) |
| **Equipo 5** | **Edwin** | Pedidos | `equipo-5-pedidos` | [pedidos.md](readme/pedidos.md) |
| **Equipo 6** | **Ubaldo** | Promociones | `equipo-6-promociones` | [promociones.md](readme/promociones.md) |
| **Equipo 8** | **Villedo** | Pagos | `equipo-8-pagos` | [pagos.md](readme/pagos.md) |
| **Equipo 9** | **Gabriel** | Envíos | `equipo-9-envios` | [envios.md](readme/envios.md) |
| **Equipo 10** | **Marcos** | Reseñas | `equipo-10-resenas` | [resenas.md](readme/resenas.md) |

---

## Pasos para Comenzar

### 1. Clonar el Repositorio (si aún no lo has hecho)

```bash
git clone https://github.com/RaulEstebanAnilesMacias222802/LSD-Metodologia.git
cd LSD-Metodologia
```

### 2. Cambiar a tu Rama de Equipo

Reemplaza `equipo-X-modulo` con tu rama correspondiente:

**Ejemplo para Equipo 1 (Usuarios):**
```bash
git checkout equipo-1-usuarios
```

### 3. Leer las Indicaciones de tu Módulo

Una vez en tu rama, abre el archivo README correspondiente a tu módulo en la carpeta `readme/`:

- **Equipo 1:** Lee [readme/usuarios.md](readme/usuarios.md)
- **Equipo 2:** Lee [readme/catalogo.md](readme/catalogo.md)
- **Equipo 3:** Lee [readme/inventario.md](readme/inventario.md)
- **Equipo 4:** Lee [readme/carrito.md](readme/carrito.md)
- **Equipo 5:** Lee [readme/pedidos.md](readme/pedidos.md)
- **Equipo 6:** Lee [readme/promociones.md](readme/promociones.md)
- **Equipo 8:** Lee [readme/pagos.md](readme/pagos.md)
- **Equipo 9:** Lee [readme/envios.md](readme/envios.md)
- **Equipo 10:** Lee [readme/resenas.md](readme/resenas.md)

### 4. Instalar y Ejecutar el Proyecto

En el README de tu módulo encontrarás instrucciones detalladas para:

1. **Instalar dependencias** - Cómo configurar tu entorno virtual
2. **Iniciar el servidor** - Cómo ejecutar la API
3. **Acceder a la documentación** - Cómo probar los endpoints

### 5. Identificar y Resolver los Bugs

En el README de tu módulo hay una sección llamada **"Revisión del PM"** que lista los problemas que debes encontrar y resolver.

---

## Estructura del Proyecto

```
LSD-Metodologia/
├── main.py                    # Archivo principal de FastAPI
├── requirements.txt           # Dependencias del proyecto
├── README.md                  # Documentación general
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

## Requisitos Técnicos

- **Python 3.8 o superior**
- **pip** (gestor de paquetes)
- **Git** (para clonar y cambiar de rama)

---

## Consejos Útiles

**Lee tu README completo** - Contiene información crucial sobre tu módulo  
**Usa la documentación interactiva** - Accede a `http://127.0.0.1:8000/docs` para probar endpoints  
**Trabaja con tu equipo** - Comunica tus hallazgos y colabora en las soluciones  
**Haz commits regulares** - Guarda tu progreso en la rama de tu equipo  

