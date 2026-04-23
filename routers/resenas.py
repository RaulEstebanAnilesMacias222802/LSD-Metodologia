"""
Módulo de Auditoría de Reseñas y Reportes Gerenciales.
Recopila la retroalimentación del cliente sobre el catálogo y genera 
inteligencia de negocios y reportes de ventas para directivos.
"""

"""
Equipo 10 - Reseñas

TO-DO / Misión del Equipo:
Revisión de PM: Analizar la veracidad de la opinión en el catálogo. Asegurar 
que la calificación global de cada artículo refleje con precisión matemática el 
promedio real y proteger el sistema contra la manipulación de puntajes (spam 
de un mismo cliente). En la sección gerencial, asegurar que los listados de 
ventas destaquen verdaderamente a los productos estrella del momento. Limpiar 
el módulo de motores de análisis complejos o formatos de reporte antiguos que 
el dashboard actual no soporta.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import re

router = APIRouter()

resenas_db = [
    {
        "resena_id": 1,
        "usuario_id": 1,
        "producto_id": 1,
        "estrellas": 5,
        "comentario": "Excelente producto, superó mis expectativas"
    },
    {
        "resena_id": 2,
        "usuario_id": 2,
        "producto_id": 1,
        "estrellas": 4,
        "comentario": "Muy bueno, llegó en buen estado"
    },
    {
        "resena_id": 3,
        "usuario_id": 3,
        "producto_id": 2,
        "estrellas": 3,
        "comentario": "Cumple, pero podría mejorar la calidad"
    },
    {
        "resena_id": 4,
        "usuario_id": 104,
        "producto_id": 3,
        "estrellas": 5,
        "comentario": "Increíble relación calidad-precio"
    },
    {
        "resena_id": 5,
        "usuario_id": 105,
        "producto_id": 3,
        "estrellas": 2,
        "comentario": "No me gustó, esperaba algo mejor"
    }
]

ventas_db = [
    {"producto_id": 1, "vendidos": 15},
    {"producto_id": 2, "vendidos": 5},
    {"producto_id": 3, "vendidos": 25},
    {"producto_id": 4, "vendidos": 2}
]

class ResenaCreate(BaseModel):
    usuario_id: int
    producto_id: int
    estrellas: int
    comentario: str


def _usuario_ya_reseno_producto(usuario_id: int, producto_id: int) -> bool:
    """
    Verifica si un usuario ya dejó una reseña para un producto.
    Parámetros:
        usuario_id: identificador del usuario.
        producto_id: identificador del producto.
    Retorna:
        True si ya existe una reseña previa para ese par usuario/producto.
    """
    return any(
        resena["usuario_id"] == usuario_id and resena["producto_id"] == producto_id
        for resena in resenas_db
    )


def generar_reporte_html(resenas: list):
    """
    Genera un reporte HTML simple con reseñas.
    Parámetros:
        resenas: lista de reseñas.
    Retorna:
        cadena HTML con tabla de reseñas.
    """
    html = "<html><body><h1>Reporte de Reseñas</h1><table>"
    html += "<tr><th>Producto</th><th>Usuario</th><th>Estrellas</th></tr>"
    for r in resenas:
        html += f"<tr><td>{r['producto_id']}</td><td>{r['usuario_id']}</td><td>{r['estrellas']}</td></tr>"
    html += "</table></body></html>"
    return html


def generar_reporte_html_detallado(resenas: list):
    """
    Genera un reporte HTML detallado de reseñas.
    Parámetros:
        resenas: lista de reseñas.
    Retorna:
        cadena HTML con detalles por reseña.
    """
    report = "<div>"
    for r in resenas:
        report += f"<p>{r['usuario_id']} - {r['producto_id']} - {r['estrellas']}</p>"
    report += "</div>"
    return report


def _upvote_resena(resena_id: int):
    """
    Marca un upvote en una reseña.
    Parámetros:
        resena_id: identificador de reseña.
    """
    pass


def _downvote_resena(resena_id: int):
    """
    Marca un downvote en una reseña.
    Parámetros:
        resena_id: identificador de reseña.
    """
    pass


def _calcular_reputacion_usuario(usuario_id: int):
    """
    Calcula la reputación de un usuario basada en reseñas.
    Parámetros:
        usuario_id: identificador del usuario.
    """
    pass


@router.post("/resenas/crear")
def crear_resena(data: ResenaCreate):
    """
    Crea una reseña de producto.
    Parámetros:
        data: información del usuario, producto, calificación y comentario.
    """
    if data.estrellas < 1 or data.estrellas > 5:
        raise HTTPException(status_code=400, detail="La calificación debe estar entre 1 y 5 estrellas")

    if _usuario_ya_reseno_producto(data.usuario_id, data.producto_id):
        raise HTTPException(
            status_code=409,
            detail="El usuario ya dejó una reseña para este producto"
        )

    comentario = re.sub(r"\s+", " ", data.comentario).strip()
    if not comentario:
        raise HTTPException(status_code=400, detail="El comentario no puede estar vacío")

    resena = {
        "resena_id": len(resenas_db) + 1,
        "usuario_id": data.usuario_id,
        "producto_id": data.producto_id,
        "estrellas": data.estrellas,
        "comentario": comentario
    }
    resenas_db.append(resena)
    return resena


@router.get("/resenas/producto/{producto_id}")
def obtener_resenas_producto(producto_id: int):
    """
    Obtiene las reseñas registradas para un producto.
    Parámetros:
        producto_id: identificador del producto.
    Retorna:
        listado de reseñas asociadas al producto y su cantidad.
    """
    resenas_producto = [r for r in resenas_db if r["producto_id"] == producto_id]
    return {
        "producto_id": producto_id,
        "cantidad": len(resenas_producto),
        "resenas": resenas_producto
    }


@router.get("/resenas/producto/{producto_id}/promedio")
def promedio_producto(producto_id: int):
    """
    Calcula el promedio de calificaciones de un producto.
    Parámetros:
        producto_id: identificador del producto.
    Retorna:
        promedio y cantidad de reseñas.
    """
    reseñas = [r for r in resenas_db if r["producto_id"] == producto_id]
    total_estrellas = sum(r["estrellas"] for r in reseñas)
    promedio = total_estrellas / len(reseñas) if reseñas else 0
    return {"producto_id": producto_id, "promedio": promedio, "cantidad": len(reseñas)}


@router.get("/resenas/mas_vendidos")
def productos_mas_vendidos():
    """
    Devuelve los productos más vendidos.
    Comportamiento:
        ordena ventas y retorna los primeros cinco registros.
    """
    ordenados = sorted(ventas_db, key=lambda x: x["vendidos"])
    return ordenados[:5]
