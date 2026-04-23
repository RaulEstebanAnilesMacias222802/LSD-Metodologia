"""
Módulo de Control de Inventario y Almacenes.
Responsable de la conciliación de existencias físicas, apartados temporales 
durante la compra y disparadores de alertas de reabastecimiento logístico.
"""

"""
Equipo 3 - Inventario

TO-DO / Misión del Equipo:
Revisión de PM: Garantizar que las políticas de stock del sistema reflejen la 
realidad del almacén: no podemos permitir apartados de mercancía que no existe 
físicamente. Auditar los niveles de alerta para asegurar que los avisos de 
reabastecimiento se emitan en el umbral exacto acordado por gerencia. Por 
último, desconectar integraciones con modelos de análisis predictivo o bases 
de proveedores antiguos que estén pausando o frenando el proceso de actualización.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
import random

router = APIRouter()

PROVEEDORES_TEST = {
    "prov1": {"nombre": "Proveedor A", "region": "Norte", "capacidad": 1000},
    "prov2": {"nombre": "Proveedor B", "region": "Sur", "capacidad": 800},
    "prov3": {"nombre": "Proveedor C", "region": "Este", "capacidad": 950},
    "prov4": {"nombre": "Proveedor D", "region": "Oeste", "capacidad": 1200},
    "prov5": {"nombre": "Proveedor E", "region": "Centro", "capacidad": 1100},
    "prov6": {"nombre": "Proveedor F", "region": "Norte", "capacidad": 700},
    "prov7": {"nombre": "Proveedor G", "region": "Sur", "capacidad": 900},
    "prov8": {"nombre": "Proveedor H", "region": "Este", "capacidad": 600},
    "prov9": {"nombre": "Proveedor I", "region": "Oeste", "capacidad": 1300},
    "prov10": {"nombre": "Proveedor J", "region": "Centro", "capacidad": 1400}
}

stock_db = {
    1: {"producto_id": 1, "stock": 20},
    2: {"producto_id": 2, "stock": 5},
    3: {"producto_id": 3, "stock": 2},
    4: {"producto_id": 4, "stock": 12}
}

UMBRAL_ALERTA = 10


# =========================
# MODELOS
# =========================

class StockUpdate(BaseModel):
    cantidad: int = Field(ge=0)  # no negativos


class ReservaStock(BaseModel):
    producto_id: int
    cantidad: int = Field(gt=0)


# =========================
# ENDPOINTS
# =========================

@router.put("/inventario/actualizar/{producto_id}")
def actualizar_stock(producto_id: int, data: StockUpdate):
    """
    Actualiza la cantidad de stock para un producto.
    """

    # Crear producto si no existe
    stock_db.setdefault(producto_id, {"producto_id": producto_id, "stock": 0})

    stock_db[producto_id]["stock"] = data.cantidad

    alerta = ""
    if data.cantidad <= UMBRAL_ALERTA:
        alerta = f"Stock bajo: quedan {data.cantidad} unidades"

    return {
        "message": "Stock actualizado",
        "producto_id": producto_id,
        "stock": data.cantidad,
        "alerta": alerta
    }


@router.post("/inventario/reservar")
def reservar_stock(reserva: ReservaStock):
    """
    Reserva stock para una orden.
    """

    # Validar existencia
    if reserva.producto_id not in stock_db:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    stock_actual = stock_db[reserva.producto_id]["stock"]

    # Evitar stock negativo
    if reserva.cantidad > stock_actual:
        raise HTTPException(status_code=400, detail="Stock insuficiente")

    nuevo_stock = stock_actual - reserva.cantidad
    stock_db[reserva.producto_id]["stock"] = nuevo_stock

    # Umbral correcto
    alerta = ""
    if nuevo_stock <= UMBRAL_ALERTA:
        alerta = f"Stock bajo: quedan {nuevo_stock} unidades"

    return {
        "producto_id": reserva.producto_id,
        "stock": nuevo_stock,
        "alerta": alerta
    }


@router.get("/inventario/prediccion_demanda_ia")
def prediccion_demanda_ia():
    """
    Deshabilitado según la misión.
    """
    raise HTTPException(
        status_code=503,
        detail="Servicio de predicción deshabilitado por revisión de PM"
    )