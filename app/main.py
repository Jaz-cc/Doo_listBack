from fastapi import FastAPI

app = FastAPI()
@app.get("/edad")
def recibir_edad(edad: str):
    return {"edad_recibida": edad}