from fastapi import APIRouter
from app.database import get_connection


router = APIRouter()

@router.get("/usuarios")
def users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result