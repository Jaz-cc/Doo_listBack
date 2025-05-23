from fastapi import APIRouter

router = APIRouter()

@router.get("/tareaconfecha")
def tareaconfecha():
    fechas = [
        {"id": 1, "Mes": "Enero", "Dias": "1, 2, 3, ..., 30"},
        {"id": 2, "Mes": "Febrero", "Dias": "1, 2, ..., 30"},
        # Agrega los demás meses igual que antes
    ]
    return fechas
