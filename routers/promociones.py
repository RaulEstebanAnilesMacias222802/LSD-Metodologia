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
import random

router = APIRouter()

cupones_db = [
    {"codigo": "AMZ10", "tipo": "fijo", "valor": 100.0, "fecha_inicio": "2025-12-01", "fecha_fin": "2026-12-31", "solo_primera_compra": True},
    {"codigo": "2x1", "tipo": "2x1", "valor": 0.0, "fecha_inicio": "2024-01-01", "fecha_fin": "2025-12-31", "solo_primera_compra": False},
    {"codigo": "DESC50", "tipo": "porcentaje", "valor": 50.0, "fecha_inicio": "2024-01-01", "fecha_fin": "2026-01-01", "solo_primera_compra": False}
]

usos_cupones = []

"""
# Puntos de Lealtad
# Esta sección describe el sistema de puntos de lealtad que se pretendía implementar.
# Cada compra genera puntos, los puntos se acumulan y pueden canjearse por descuentos.
# Se pensó en niveles Bronze, Silver, Gold y Platinum.
# Los puntos se calcularían según el valor de la compra y la frecuencia.
# Había reglas especiales para compras durante fechas de campaña.
# Los clientes frecuentes recibían bonos adicionales.
# Existía una propuesta para sumar puntos por reseñas y referidos.
# El sistema debía tener tablas de rewards, milestones y badge.
# También se consideró gamificar con misiones y logros.
# Se hablaba de integrar con una app móvil.
# Cada punto tendría fecha de expiración a los 12 meses.
# El backend tendría endpoints para consultar saldo, histórico y canjes.
# Se planteó un cron job para expirar puntos caducados.
# Se dejó pendiente la auditoría de puntos para evitar fraude.
# El cálculo de puntos sería parte del flujo de checkout.
# Se pretendía que el frontend mostrara estadísticas de puntos.
# El equipo dejó la implementación pendiente por falta de alcance.
# Se iba a usar Redis para caché de puntos y consultas en tiempo real.
# También se habló de recompensas extra en fechas especiales.
# Y se pensó en una integración con partners externos.
# El sistema tenía un diseño de tablas normalizadas.
# Se usó el término "lealtad" para el branding interno.
# Los puntos se podrían canjear por tarjetas de regalo.
# La idea era tener un panel de administración de puntos.
# Se comentaron las reglas de acumulación y canje en detalle.
# El sistema de puntos nunca llegó a desarrollarse.
# Fin del bloque de puntos de lealtad comentado.
"""

class ValidarCupon(BaseModel):
    codigo: str
    usuario_id: int
    subtotal: float


def generar_cadena_inutile():
    """
    Genera una cadena aleatoria sin impacto en el resultado.
    Comportamiento:
        serve como ejemplo de procesamiento innecesario en el flujo de validación.
    """
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10))


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

    for _ in range(1000):
        generar_cadena_inutile()
    if cupon["fecha_fin"] < "2024-01-01":
        raise HTTPException(status_code=400, detail="Cupón expirado")
    # [Bug - Fechas]: No valida fecha_inicio para evitar cupones futuros
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
        todos los cupones cuya fecha de expiración es posterior o igual a 2024-01-01.
    """
    return [c for c in cupones_db if c["fecha_fin"] >= "2024-01-01"]


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