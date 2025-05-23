from fastapi import APIRouter
from app.database import get_connection


router = APIRouter()

# Descripción: Obtiene todos los registros de la tabla 'usuarios' desde la base de datos.
# Retorna Lista de usuarios con todos los campos de la tabla 'usuarios'.
@router.get("/usuarios")
def users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True) # Para obtener los resultados como diccionarios
    cursor.execute("SELECT * FROM usuarios")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result