from fastapi import APIRouter
from app.database import get_connection
from pydantic import BaseModel

router = APIRouter()

# Descripción: Devuelve una lista fija de tareas de ejemplo.
# Retorna la Lista de tareas con id, titulo, descripcion, hora y status.
@router.get("/añadirtarea")
def tarea():
    tareas = [
        {"id": 1, "titulo": "Comprar chelas", "descripcion": "Ir a la tienda", "hora": "1:00pm", "status": "No realizada"},
        {"id": 2, "titulo": "Bañar a Tobi", "descripcion": "Usar shampoo antipulgas", "hora": "3:30pm", "status": "Realizada"},
        {"id": 3, "titulo": "Ir al GYM", "descripcion": "Recuerda llevar agua", "hora": "5:00pm", "status": "Pendiente"},
    ]
    return tareas

# Descripción: Retorna una lista diferente de tareas de ejemplo.
# Lista de tareas con id, titulo, descripcion, hora y status.
@router.get("/todas")
def obtener_todas_las_tareas():
    tareass = [
        {"id": 1, "titulo": "Hacer compras", "descripcion": "Comprar leche y pan", "hora": "10:00am", "status": "Pendiente"},
        {"id": 2, "titulo": "Estudiar", "descripcion": "Repasar FastAPI", "hora": "2:00pm", "status": "Completado"},
        {"id": 3, "titulo": "Ir al gimnasio", "descripcion": "Entrenamiento de pierna", "hora": "6:00pm", "status": "Pendiente"},
    ]
    return tareass

class Tarea(BaseModel):
    titulo:str
    descripcion:str
    hora:str
    status:str

# Descripción: Recibe una tarea nueva y devuelve un mensaje de confirmación junto con los datos enviados.
# Retorna el Mensaje de éxito y los datos de la tarea añadida.
@router.post("/añadir_tarea")
def añadir_tarea(tarea: Tarea):
    return {"mensaje": "Tarea añadida correctamente", **tarea.dict()}