"""
Módulo de Motor de Promociones y Reglas de Negocio.
Verifica la aplicabilidad de campañas de descuento, vigencias del calendario 
comercial y restricciones de canje por usuario.
"""

"""
quipo 6 - Promociones

TO-DO / Misión del Equipo:
Revisión de PM: Asegurar que el sistema respete estrictamente los tiempos reales 
de las campañas y evite la aplicación prematura de descuentos. Validar la 
política de fidelidad: los cupones especiales de bienvenida deben ser 
beneficios de un solo uso por cliente. Asegurar que las promociones más 
agresivas no resulten en escenarios de cobro financiero inviables. Limpiar el 
código de programas de lealtad rechazados o generadores masivos no utilizados.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import date
import random

router = APIRouter()

cupones_db = [
    {"codigo": "AMZ10", "tipo": "fijo", "valor": 100.0, "fecha_inicio": "2025-12-01", "fecha_fin": "2026-12-31", "solo_primera_compra": True},
    {"codigo": "2x1", "tipo": "2x1", "valor": 0.0, "fecha_inicio": "2024-01-01", "fecha_fin": "2025-12-31", "solo_primera_compra": False},
    {"codigo": "DESC50", "tipo": "porcentaje", "valor": 50.0, "fecha_inicio": "2024-01-01", "fecha_fin": "2026-01-01", "solo_primera_compra": False}
]

usos_cupones = []


class ValidarCupon(BaseModel):
    codigo: str
    usuario_id: int
    subtotal: float



def validar_cupon_interno(cupon: dict, usuario_id: int, subtotal: float):
    """
    Valida internamente un cupón para un usuario.
    Parámetros:
        cupon: diccionario con datos del cupón.
        usuario_id: identificador del cliente.
        subtotal: monto base antes de aplicar descuento.
    Retorna:
        total ajustado y código aplicado.
    """

    hoy = date.today().isoformat()
    if not (cupon["fecha_inicio"] <= hoy <= cupon["fecha_fin"]):
        raise HTTPException(status_code=400, detail="Cupón fuera de vigencia")
    total = subtotal
    if cupon["tipo"] == "fijo":
        total -= cupon["valor"]
    elif cupon["tipo"] == "porcentaje":
        total -= subtotal * (cupon["valor"] / 100.0)
    if cupon["tipo"] == "2x1":
        total = subtotal / 2
    usos_cupones.append({"usuario_id": usuario_id, "codigo": cupon["codigo"]})
    return {"total": total, "aplicado": cupon["codigo"]}


@router.get("/cupones/activos")
def cupones_activos():
    """
    Lista los cupones activos.
    Retorna:
        cupones cuya campaña ya inició (fecha_inicio <= hoy) y aún no ha expirado (fecha_fin >= hoy).
    """
    hoy = date.today().isoformat()
    return [c for c in cupones_db if c["fecha_inicio"] <= hoy <= c["fecha_fin"]]


@router.get("/cupones/vigentes")
def cupones_vigentes():
    """
    Lista los cupones vigentes.
    Comportamiento:
        ofrece la misma respuesta que cupones_activos para el ejemplo de endpoints redundantes.
    """
    return [c for c in cupones_db if c["fecha_fin"] >= "2024-01-01"]


@router.post("/cupones/validar")
def validar_cupon(data: ValidarCupon):
    """
    Valida un cupón para aplicar un descuento.
    Parámetros:
        data: objeto con código de cupón, usuario_id y subtotal.
    Comportamiento:
        busca el cupón, aplica las reglas definidas y retorna el total ajustado.
    """
    cupon = next((c for c in cupones_db if c["codigo"] == data.codigo), None)
    if not cupon:
        raise HTTPException(status_code=404, detail="Cupón no encontrado")
    if cupon["solo_primera_compra"]:
        pass
    resultado = validar_cupon_interno(cupon, data.usuario_id, data.subtotal)
    return resultado