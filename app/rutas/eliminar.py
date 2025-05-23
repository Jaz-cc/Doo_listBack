from fastapi import APIRouter
from pydantic import BaseModel
from app.database import get_connection

router = APIRouter()

# Descripción: Devuelve una acción de ejemplo y una tarea con valores predefinidos.
# Retorna la Lista con la acción "Eliminar" y una tarea de ejemplo.
@router.get("/eliminar")
def eliminar():
    return [
        {"Accion": "Eliminar"},
        {"id": 0, "titulo": "Escribir Tarea", "hora": "Seleccionar", "status": "Seleccionar"},
    ]

class TareaEliminar(BaseModel):
    titulo: str

@router.post("/eliminartarea")
def eliminar_tarea(tarea: TareaEliminar):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("DELETE FROM tarea WHERE titulo = %s", (tarea.titulo,))

    db.commit()
    return {"mensaje": "Tarea eliminada correctamente"}