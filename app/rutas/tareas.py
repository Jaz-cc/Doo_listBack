from fastapi import APIRouter

router = APIRouter()

@router.get("/añadirtarea")
def tarea():
    tareas = [
        {"id": 1, "titulo": "Comprar chelas", "descripcion": "Ir a la tienda", "hora": "1:00pm", "status": "No realizada"},
        {"id": 2, "titulo": "Bañar a Tobi", "descripcion": "Usar shampoo antipulgas", "hora": "3:30pm", "status": "Realizada"},
        {"id": 3, "titulo": "Ir al GYM", "descripcion": "Recuerda llevar agua", "hora": "5:00pm", "status": "Pendiente"},
    ]
    return tareas


@router.get("/todas")
def obtener_todas_las_tareas():
    tareass = [
        {"id": 1, "titulo": "Hacer compras", "descripcion": "Comprar leche y pan", "hora": "10:00am", "status": "Pendiente"},
        {"id": 2, "titulo": "Estudiar", "descripcion": "Repasar FastAPI", "hora": "2:00pm", "status": "Completado"},
        {"id": 3, "titulo": "Ir al gimnasio", "descripcion": "Entrenamiento de pierna", "hora": "6:00pm", "status": "Pendiente"},
    ]
    return tareass
