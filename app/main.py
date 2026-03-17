from fastapi import FastAPI
from app.database import Base,engine
from app.route.usuario import usuario
from app.route.passageiro import passageiro

Base.metadata.create_all(bind=engine)

app= FastAPI() #inicia a aplicação FastAPI

app.include_router(usuario, tags=["Usuários"])
app.include_router(passageiro, tags=["Passageiros"])

@app.get("/")
async def health_check():
    return {"status": "API Online"}