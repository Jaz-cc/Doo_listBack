from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.database import get_connection 
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet

router = APIRouter()

@router.get("/reporte-pdf", tags=["Reportes"])
def generar_reporte_pdf():
    #Leer tareas 
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM tarea")
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()

    #Contar tareas por estado
    conteo = {"Realizada": 0, "Pendiente": 0, "No realizada": 0}
    for fila in resultados:
        estado = fila[0]  #El estado viene como una tupla
        if estado in conteo:
            conteo[estado] += 1

    estados = list(conteo.keys()) # ["Realizada", "Pendiente", "No realizada"]
    cantidades = list(conteo.values())

    #Gráfica de pastel
    plt.pie(cantidades, labels=estados, autopct='%1.1f%%')
    plt.title("Distribución de Tareas")
    plt.savefig("pastel.png") # Guardamos como imagen
    plt.close()

    #Gráfica de barras
    plt.bar(estados, cantidades, color="skyblue")
    plt.title("Tareas por Estado")
    plt.savefig("barras.png")
    plt.close()

    #Crear PDF con reportlab
    doc = SimpleDocTemplate("reporte.pdf", pagesize=letter) # Configura el tamaño de hoja
    estilos = getSampleStyleSheet() # Plantilla de estilos para texto
    partes = [] # se agregan los elementos del PDF

    partes.append(Paragraph("Reporte de Tareas", estilos["Title"]))
    partes.append(Spacer(1, 12)) # Espacio entre secciones
    partes.append(Paragraph("Gráfico de Pastel:", estilos["Heading2"]))
    partes.append(Image("pastel.png", width=400, height=300))
    partes.append(Spacer(1, 12))
    partes.append(Paragraph("Gráfico de Barras:", estilos["Heading2"]))
    partes.append(Image("barras.png", width=400, height=300))

    doc.build(partes) # Construimos el PDF con todos los elementos agregados

     #Devolver el PDF como descarga
    return FileResponse("reporte.pdf", media_type="application/pdf", filename="reporte_tareas.pdf")
