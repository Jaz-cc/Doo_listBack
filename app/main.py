from fastapi import FastAPI
from .database import get_connection

app = FastAPI()

@app.get("/verificar_conexion")
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

# Este codigo es solo para verificar el estado de conexion de la base de datos

@app.get("/edad")
def recibir_edad(edad: str):
    return {"edad_recibida": edad}

@app.get("/")
def leer_root():
    return {"mensaje": "Hola, este es el backend sin base de datos"}

@app.get("/usuarios")
def users():
    usersfakes = [
        {"id": 1, "nombre": "Jazmin"},
        {"id": 2, "nombre": "Jesus"},
        {"id": 3, "nombre": "Raul"},
    ]
    return usersfakes

# @app.get("/continentes")
# def continente():
#     continentes = [
#         {"id":1, "continente": "America del norte"},
#         {"id":2, "continente": "America del sur"},
#         {"id":3, "continente": "Africa"},
#         {"id":4, "continente": "Europa"},
#         {"id":5, "continente": "Oceania"},
#         {"id":6, "continente": "Antartida"},
#         {"id":7, "continente": "Asia"},
#     ]
#     return continentes

# Endpoint Añadir Tarea
@app.get("/añadirtarea")
def tarea():
    tareas = [
       {"id": 1, "tarea": "Comprar chelas", "hora":"1:00pm", "status":"No realizada"},
       {"id": 2, "tarea": "Bañar a Tobi","hora":"3:30pm", "status":"Realizada"},
       {"id": 3, "tarea": "Ir al GYM","hora":"5:00pm", "status":"Pendiente"},
    ]
    return tareas

# Endpoint Eliminar
@app.get("/Eliminar")
def Elimar():
    EliminarTarea = [
        {"Accion": "Eliminar"},
        {"id": 0, "tarea": "Escribir Tarea", "hora":"Seleccionar", "status":"Seleccionar"},
    ]
    return EliminarTarea


# Endpoint Editar
@app.get("/Editar")
def Editar():
    EditarTarea = [
        {"Accion": "Editar Tarea"},
        {"id": 0, "tarea": "Renombrar Tarea", "hora":"Seleccionar", "status":"Seleccionar"},
    ]
    return EditarTarea

# Endpoint Completadas
@app.get("/Completadas")
def Completadas():
    TareasCompletadas = [
        {"Accion": "!FELICIDADES¡TAREA COMPLETADA."},
        {"id": 0, "tarea": "Tarea Completada", "hora":"Finalizado", "status":"Finalizado"},
    ]
    return TareasCompletadas

# Endpoint Con Fecha
@app.get("/tareaconfecha")
def tareaconfecha():
    fechas = [
       {"id": 1, "Mes": "Enero", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"},
       {"id": 2, "Mes": "Febrero", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"},
       {"id": 3, "Mes": "Marzo", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"},
       {"id": 4, "Mes": "Abril", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"},
       {"id": 5, "Mes": "Mayo", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"},
       {"id": 6, "Mes": "Junio", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"},
       {"id": 7, "Mes": "Julio", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"},
       {"id": 8, "Mes": "Agosto", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"},
       {"id": 9, "Mes": "Septiembre", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"},
       {"id": 10, "Mes": "Octubre", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"},
       {"id": 11, "Mes": "Noviembre", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"},
       {"id": 12, "Mes": "Diciembre", "Dias":"1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"
                                        " 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,"
                                        " 21, 22, 23, 24, 25, 26, 27, 28, 29, 30"},
    ]
    return fechas