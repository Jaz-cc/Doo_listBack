from fastapi import APIRouter
from pydantic import BaseModel
from app.database import get_connection

router = APIRouter()

# Descripción: Devuelve una acción de ejemplo y una tarea editable con valores predefinidos.
# Retorna la Lista con la acción "Editar Tarea" y una tarea de ejemplo.
@router.get("/editar")
def editar():
    return [
        {"Accion": "Editar Tarea"},
        {"id": 0, "tarea": "Renombrar Tarea", "hora": "Seleccionar", "status": "Seleccionar"},
    ]

# Modelo para editar una tarea
# Campos requeridos:
# id,tarea, hora, status
class TareaEditada(BaseModel):
    id: int
    tarea:str
    hora:str
    status:str

@router.post("/editartarea")
def editar_tarea(tarea: TareaEditada):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("UPDATE tarea SET titulo = %s, hora = %s, status = %s WHERE id = %s",
                   (tarea.tarea, tarea.hora, tarea.status, tarea.id))
    db.commit()
    return {"mensaje": "Tarea editada correctamente"}