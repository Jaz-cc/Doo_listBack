from fastapi import APIRouter
from fastapi.responses import FileResponse
import csv
from app.database import get_connection

router = APIRouter()
# Ruta para obtener estadísticas generales
@router.get("/estadisticas")
def obtener_estadisticas():
    db = get_connection()
    cursor = db.cursor(dictionary=True) # Creamos un cursor que devuelve diccionarios

    #contamos el total de las tareas registradas
    cursor.execute("SELECT COUNT(*) AS total FROM tarea")
    total = cursor.fetchone()["total"]
    #contamos las tareas completadas
    cursor.execute("SELECT COUNT(*) AS completadas FROM tarea WHERE LOWER(status) IN ('realizada')")
    completadas = cursor.fetchone()["completadas"]
    #calculamos el porcentaje del avance 
    progreso = int((completadas / total) * 100) if total else 0

    return {
        "total": total,
        "completadas": completadas,
        "progreso": progreso
    }
#ruta para contar las tareas agrupadas por estado
@router.get("/estado-estadistica")
def contar_por_estado():
    db = get_connection()
    cursor = db.cursor(dictionary=True)

    #agrupamos las tareas por estado y contamos cuantas hay por cada status
    cursor.execute("SELECT status, COUNT(*) AS cantidad FROM tarea GROUP BY status")
    estados = cursor.fetchall()

    return estados

#ruta para exportar las tareas a csv
@router.get("/exportar-csv")
def exportar_csv():
    db = get_connection()
    cursor = db.cursor(dictionary=True)

    #consultar tareas para la bd
    cursor.execute("SELECT id, titulo, descripcion, hora, status FROM tarea")
    tareas = cursor.fetchall()

    total_tareas=len(tareas)
    completadas = 0
    
    #Creamos un diccionario para contar cuántas tareas hay por estado
    #calculamos conteos por estado
    conteo = {}
    for tarea in tareas:
        estado = tarea["status"]
        conteo[estado] = conteo.get(estado, 0) + 1
        if estado.lower() in ["completado","realizada"]:
            completadas += 1
    #Calculamos el porcentaje de tareas completadas
    porcentaje = round((completadas/total_tareas)*100,2) if total_tareas > 0 else 0

    #crear archivo csv
    ruta_csv = "tareas.csv"

    #escribir archivo csv
    with open(ruta_csv, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["ID", "Título", "Descripción", "Hora", "Status"])  # Encabezados
        #tabla tareas
        for tarea in tareas:
            writer.writerow([
                tarea["id"],
                tarea["titulo"],
                tarea["descripcion"],
                tarea["hora"],
                tarea["status"]
            ])
        #linea vacia
        writer.writerow([])

        #agregamos el resumen por estado
        writer.writerow(["Resumen de tareas por estado"])
        for estado, cantidad in conteo.items():
            writer.writerow([estado, cantidad])
        
        #Porcentaje
        writer.writerow([])
        writer.writerow(["Porcentaje de tareas completadas", f"{porcentaje}%"])

    #Retornamos el archivo para que se pueda descargar desde Swagger o el frontend
    return FileResponse(
        path=ruta_csv,
        filename="tareas.csv",
        media_type="text/csv"
    )
exportar_router = router