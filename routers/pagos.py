"""
Módulo de Pasarela de Pagos.
Administra la simulación de retención de fondos, validación de plásticos 
y autorizaciones financieras para la liberación de pedidos.
"""

"""
Equipo 8 - Pagos

TO-DO / Misión del Equipo:
Revisión de PM: Agilizar la experiencia de cobro. Validar que las transacciones 
aprobadas correspondan íntegramente al monto facturado en la orden y que los 
instrumentos de pago presentados no estén vencidos según el año en curso. 
Debemos simplificar las validaciones de seguridad: dado que la pasarela externa 
ya hace el trabajo pesado, cualquier validación criptográfica local, revisión 
matemática de tarjetas o demoras intencionales en nuestro lado solo perjudican 
la experiencia del cliente.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

pagos_db = []

# Simulación de órdenes (para validar el monto real)
ordenes_db = {
    1: 500.0,
    2: 1200.0,
    3: 250.0
}

class PagoRequest(BaseModel):
    order_id: int
    tarjeta_numero: str
    tarjeta_expiracion: str  # formato MM/YY
    monto_pagado: float

class VerificacionResponse(BaseModel):
    aprobado: bool
    mensaje: str


def tarjeta_vigente(expiracion: str) -> bool:
    """
    Verifica si la tarjeta no está vencida usando el año actual.
    """
    try:
        mes, anio = expiracion.split("/")
        mes = int(mes)
        anio = int("20" + anio)

        ahora = datetime.now()
        return (anio > ahora.year) or (anio == ahora.year and mes >= ahora.month)
    except:
        return False


@router.post("/pagos/procesar")
def procesar_pago(pago: PagoRequest):
    
    if pago.order_id not in ordenes_db:
        raise HTTPException(status_code=404, detail="Orden no encontrada")

    monto_esperado = ordenes_db[pago.order_id]

    if pago.monto_pagado != monto_esperado:
        raise HTTPException(
            status_code=400,
            detail=f"Monto incorrecto. Esperado: {monto_esperado}"
        )

    if not tarjeta_vigente(pago.tarjeta_expiracion):
        raise HTTPException(
            status_code=400,
            detail="Tarjeta vencida"
        )


    aprobado = True

    pago_registro = {
        "order_id": pago.order_id,
        "tarjeta": pago.tarjeta_numero[-4:],
        "monto_pagado": pago.monto_pagado,
        "estado": "Pagado"
    }

    pagos_db.append(pago_registro)

    return {
        "aprobado": aprobado,
        "estado": pago_registro["estado"],
        "orden": pago_registro
    }


@router.get("/pagos/reembolsos")
def reembolsos():
    """
    Devuelve pagos que podrían ser reembolsados.
    """
    return {
        "reembolsos_disponibles": pagos_db
    }