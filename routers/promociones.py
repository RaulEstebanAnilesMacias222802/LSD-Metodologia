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
from datetime import datetime
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

@router.get("/cupones")
def listar_cupones():
    return cupones_db
@router.get("/cupones/activos")
def cupones_activos():
    """
    Lista los cupones activos.
    Retorna:
        cupones cuya campaña ya inició (fecha_inicio <= hoy) y aún no ha expirado (fecha_fin >= hoy).
    """
    hoy = date.today().isoformat()
    return [c for c in cupones_db if c["fecha_inicio"] <= hoy <= c["fecha_fin"]]


@router.post("/cupones/validar/{codigo}")
def validar_cupon(codigo: str, data: ValidarCupon):
    """
    Valida un cupón para aplicar un descuento.
    Parámetros:
        data: objeto con código de cupón, usuario_id y subtotal.
    Comportamiento:
        busca el cupón, aplica las reglas definidas y retorna el total ajustado.
    """
    cupon = next((c for c in cupones_db if c["codigo"] == codigo), None)
    if not cupon:
        raise HTTPException(status_code=404, detail="Cupón no encontrado")
    
    if cupon["solo_primera_compra"]:
        ya_usado = any(
            u["usuario_id"] == data.usuario_id and u["codigo"] == cupon["codigo"]
            for u in usos_cupones
        )
        if ya_usado:
            raise HTTPException(status_code=400, detail="Este cupón solo puede usarse en la primera compra")

    resultado = validar_cupon_interno(cupon, data.usuario_id, data.subtotal)
    return resultado


# ──────────────────────────────────────────────
# Sistema de Puntos de Lealtad (en memoria)
# ──────────────────────────────────────────────

puntos_db: dict = {}          # usuario_id → puntos acumulados
historial_puntos: list = []   # registro de movimientos

PUNTOS_POR_PESO = 1        # 1 punto por cada peso gastado
VALOR_PUNTO     = 0.10     # cada punto vale $0.10 MXN al canjear


class AplicarDescuento(BaseModel):
    usuario_id: int
    subtotal: float
    codigo_cupon: Optional[str] = None


class CanjearPuntos(BaseModel):
    usuario_id: int
    puntos_a_canjear: int


# ── Tarea #12 ─────────────────────────────────
@router.post("/aplicar_descuento")
def aplicar_descuento(data: AplicarDescuento):
    """
    Aplica un cupón (si se proporciona) y calcula los puntos ganados por la compra.
    Parámetros:
        data: objeto con usuario_id, subtotal y código de cupón opcional.
    Retorna:
        total_final, descuento_aplicado y puntos_ganados.
    """
    total = data.subtotal
    descuento = 0.0
    cupon_aplicado = None

    if data.codigo_cupon:
        cupon = next(
            (c for c in cupones_db if c["codigo"] == data.codigo_cupon), None
        )
        if cupon:
            hoy = datetime.now().strftime("%Y-%m-%d")

            if hoy < cupon["fecha_inicio"]:
                raise HTTPException(
                    status_code=400,
                    detail="El cupón aún no está vigente"
                )
            if hoy > cupon["fecha_fin"]:
                raise HTTPException(
                    status_code=400,
                    detail="Cupón expirado"
                )

            if cupon["tipo"] == "fijo":
                descuento = cupon["valor"]
            elif cupon["tipo"] == "porcentaje":
                descuento = data.subtotal * (cupon["valor"] / 100.0)
            elif cupon["tipo"] == "2x1":
                descuento = data.subtotal / 2

            total = max(0.0, data.subtotal - descuento)
            cupon_aplicado = cupon["codigo"]

    # Sumar puntos ganados por esta compra
    puntos_ganados = int(total * PUNTOS_POR_PESO)
    puntos_db[data.usuario_id] = puntos_db.get(data.usuario_id, 0) + puntos_ganados
    historial_puntos.append({
        "usuario_id": data.usuario_id,
        "tipo": "ganado",
        "puntos": puntos_ganados,
        "fecha": datetime.now().strftime("%Y-%m-%d")
    })

    return {
        "total_final": round(total, 2),
        "descuento_aplicado": round(descuento, 2),
        "cupon_usado": cupon_aplicado,
        "puntos_ganados": puntos_ganados
    }


# ── Tarea #13 ─────────────────────────────────
@router.get("/puntos/{usuario_id}")
def obtener_puntos(usuario_id: int):
    """
    Consulta los puntos acumulados de un usuario y su historial.
    Parámetros:
        usuario_id: identificador del cliente.
    Retorna:
        puntos_acumulados e historial de movimientos.
    """
    puntos = puntos_db.get(usuario_id, 0)
    historial = [h for h in historial_puntos if h["usuario_id"] == usuario_id]

    return {
        "usuario_id": usuario_id,
        "puntos_acumulados": puntos,
        "historial": historial
    }


# ── Tarea #14 ─────────────────────────────────
@router.post("/canjear_puntos")
def canjear_puntos(data: CanjearPuntos):
    """
    Canjea puntos de un usuario por un descuento en pesos.
    Parámetros:
        data: objeto con usuario_id y puntos_a_canjear.
    Retorna:
        descuento_obtenido en pesos y puntos_restantes.
    """
    saldo = puntos_db.get(data.usuario_id, 0)

    if data.puntos_a_canjear <= 0:
        raise HTTPException(
            status_code=400,
            detail="La cantidad de puntos a canjear debe ser mayor a 0"
        )
    if data.puntos_a_canjear > saldo:
        raise HTTPException(
            status_code=400,
            detail=f"Puntos insuficientes. Saldo actual: {saldo}"
        )

    descuento = round(data.puntos_a_canjear * VALOR_PUNTO, 2)
    puntos_db[data.usuario_id] = saldo - data.puntos_a_canjear

    historial_puntos.append({
        "usuario_id": data.usuario_id,
        "tipo": "canjeado",
        "puntos": -data.puntos_a_canjear,
        "fecha": datetime.now().strftime("%Y-%m-%d")
    })

    return {
        "descuento_obtenido": descuento,
        "puntos_restantes": puntos_db[data.usuario_id]
    }
    return resultado

