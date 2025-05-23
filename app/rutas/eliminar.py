from fastapi import APIRouter

router = APIRouter()

@router.get("/eliminar")
def eliminar():
    return [
        {"Accion": "Eliminar"},
        {"id": 0, "tarea": "Escribir Tarea", "hora": "Seleccionar", "status": "Seleccionar"},
    ]