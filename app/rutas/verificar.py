from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

# Modelo de entrada para una tarea
class TareaInput(BaseModel):
    titulo: Optional[str] = None
    descripcion: str  
    
@router.post("/verificar-campos")
def verificar_campos(tarea: TareaInput):
    if not tarea.descripcion:
        raise HTTPException(status_code=400, detail="La descripción es obligatoria.")
    
    return {
        "mensaje": "Datos recibidos correctamente.",
        "titulo": tarea.titulo,
        "descripcion": tarea.descripcion
    }
