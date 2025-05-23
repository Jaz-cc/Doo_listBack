from fastapi import APIRouter
from app.database import get_connection

router = APIRouter()

@router.get("/verificar_conexion")
def verificar_conexion():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()
        return {"conexion": "exitosa", "resultado": resultado}
    except Exception as e:
        return {"conexion": "fallida", "error": str(e)}