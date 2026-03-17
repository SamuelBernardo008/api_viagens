from fastapi import FastAPI
from app.database import Base,engine
from app.route.usuario import usuario
from app.route.passageiro import passageiro
from app.route.motorista import motorista
from app.route.veiculo import veiculo

# from app.models.classe import ClasseModel
# from app.models.combustivel import CombustivelModel

Base.metadata.create_all(bind=engine)

app= FastAPI() #inicia a aplicação FastAPI

app.include_router(usuario, tags=["Usuários"])
app.include_router(passageiro, tags=["Passageiros"])
app.include_router(motorista, tags=["Motoristas"])
app.include_router(veiculo, tags=["Veículos"])


@app.get("/")
async def health_check():
    return {"status": "API Online"}