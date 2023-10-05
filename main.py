from fastapi import FastAPI

app = FastAPI() #variable

@app.get("/")  #definir ruta
def read_root():
    return {"message": "Hola comunidad Humai"} #llaves porque devueleve un json, o un diccionario de python en este caso

