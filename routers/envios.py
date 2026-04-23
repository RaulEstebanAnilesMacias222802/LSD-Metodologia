"""
Módulo de Logística y Rutas de Envío.
Encargado de la asignación de paqueterías, generación de guías de rastreo 
y cálculo de volumetría/peso para costos de distribución.
"""

"""
Equipo 9 - Envíos

TO-DO / Misión del Equipo:
Revisión de PM: Evaluar la correcta aplicación de nuestras políticas de entrega. 
Comprobar que los incentivos de envío gratuito se otorguen basados en el volumen 
financiero de compra del cliente, no en características físicas del paquete. 
Garantizar que ningún pedido pase a etapa de tránsito sin contar con información 
de destino válida. Retirar integraciones externas de monitoreo que no hayan sido 
solicitadas oficialmente o cotizadores multimoneda que no apliquen a nuestro mercado.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# endpoint 5: se retiró la variable CODIGOS_POSTALES_TEST 

pedidos_db = [
    {"pedido_id": 1, "direccion": "Av. Reforma 123", "peso": 50, "precio": 1200.0, "estado_envio": "Pendiente"},
    {"pedido_id": 2, "direccion": None, "peso": 5, "precio": 300.0, "estado_envio": "Pendiente"}
]

class CotizarEnvio(BaseModel):
    pedido_id: int
    peso: float
# endpoint 6: se retiro distancia_km

class CambiarEstadoEnvio(BaseModel):
    pedido_id: int
    estado: str

@router.post("/envios/cotizar")
def cotizar_envio(datos: CotizarEnvio):
    """
    Calcula una cotización de envío para un pedido.
    Parámetros:
        datos: objeto con pedido_id, peso y distancia.
    Retorna:
        costo en MXN junto con la moneda base.
    """
    pedido = next((p for p in pedidos_db if p["pedido_id"] == datos.pedido_id), None)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    
    # endpoint 1: se retiró la llamada a la función de clima 
    
    base = 100.0
    peso_extra = max(0, datos.peso - 10)
    costo = base * (peso_extra * 10)
    
    # endoint 3: envío gratis basado en el precio
    if pedido["precio"] >= 1000.0:
        costo = 0.0
        
    # endpoint 2: se eliminó el cotizador multimoneda
    return {
        "pedido_id": datos.pedido_id,
        "costo_mxn": costo,
        "moneda": "MXN"
    }

@router.patch("/envios/estado")
def cambiar_estado_envio(update: CambiarEstadoEnvio):
    """
    Actualiza el estado del envío de un pedido.
    Parámetros:
        update: objeto con pedido_id y estado.
    Comportamiento:
        modifica el estado de envío en memoria y retorna el registro actualizado.
    """
    pedido = next((p for p in pedidos_db if p["pedido_id"] == update.pedido_id), None)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
        
    # endpoint 4: validación de dirección para estado
    if update.estado == "En tránsito" and not pedido.get("direccion"):
        raise HTTPException(status_code=400, detail="No se puede pasar a tránsito sin una dirección de destino válida")
        
    pedido["estado_envio"] = update.estado
    return pedido