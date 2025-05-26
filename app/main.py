from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import get_connection

from app.rutas.tareas import router as tareas_router
from app.rutas.conexion import router as conexion_router
from app.rutas.usuarios import router as usuarios_router
from app.rutas.eliminar import router as eliminar_router
from app.rutas.editar import router as editar_router
from app.rutas.completadas import router as completadas_router
from app.rutas.fechas import router as fechas_router
from app.rutas.verificar import router as verificar_router
from app.rutas.exportar import exportar_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir todos los routers
app.include_router(conexion_router)
app.include_router(usuarios_router)
app.include_router(tareas_router)
app.include_router(eliminar_router)
app.include_router(editar_router)
app.include_router(completadas_router)
app.include_router(fechas_router)
app.include_router(verificar_router)
app.include_router(exportar_router)

@app.get("/")
def root():
    return {"mensaje": "Hola, este es el backend de la API de tareas"}