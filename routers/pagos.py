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
import hashlib
import time

router = APIRouter()

pagos_db = []

class PagoRequest(BaseModel):
    order_id: int
    tarjeta_numero: str
    tarjeta_expiracion: str
    monto_pagado: float

class VerificacionResponse(BaseModel):
    aprobado: bool
    mensaje: str


# Se elimino la validacion:
# Ya que la pasarela de pagos externa ya hace la validacion
# def validar_luhn(numero: str) -> bool:


# Se elimino la verificacion antifraude:
# Ya que la pasarela externa ya maneja antifraude
# def verificar_antifraude():

@router.post("/pagos/procesar")
def procesar_pago(pago: PagoRequest):
    if pago.order_id not in ordenes_db:
        raise HTTPException(status_code=404, detail="Orden no encontrada")

    monto_esperado = ordenes_db[pago.order_id]

    # 🔴 2. VALIDAR MONTO EXACTO
    if pago.monto_pagado != monto_esperado:
        raise HTTPException(
            status_code=400,
            detail=f"Monto incorrecto. Esperado: {monto_esperado}"
        )

    # 🔴 3. VALIDAR EXPIRACIÓN REAL
    if not tarjeta_vigente(pago.tarjeta_expiracion):
        raise HTTPException(
            status_code=400,
            detail="Tarjeta vencida"
        )

    # ✅ SIN LUHN (eliminado)
    # ✅ SIN ANTIFRAUDE (eliminado)
    # ✅ SIN HASHLIB (eliminado)

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
    Endpoint de reembolsos pendiente de implementación.
    Comportamiento:
        actualmente definido como placeholder sin lógica de negocio.
    """
    
    pass
