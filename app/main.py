from fastapi import FastAPI
from app.database import Base,engine
from app.route.usuario import usuario
from app.route.passageiro import passageiro
from app.route.motorista import motorista
from app.route.veiculo import veiculo
from app.route.motorista_veiculo import motorista_veiculo
from app.route.classe import classe
from app.route.modelo_veiculo import modelo_veiculo
from app.route.combustivel import combustivel
from app.route.servico import servico
from app.route.avaliacao import avaliacao
from app.route.metodo_pagamento import metodo_pagamento
from app.route.pagamento import pagamento
from app.route.corrida import corrida


Base.metadata.create_all(bind=engine)

app= FastAPI() #inicia a aplicação FastAPI

app.include_router(usuario, prefix="/usuarios", tags=["Usuários"])
app.include_router(passageiro, prefix="/passageiros", tags=["Passageiros"])
app.include_router(motorista, prefix="/motoristas", tags=["Motoristas"])
app.include_router(combustivel, prefix="/combustiveis", tags=["Combustíveis"])
app.include_router(classe, prefix="/classes", tags=["Classes de Veículos"])
app.include_router(modelo_veiculo, prefix="/modelos", tags=["Modelos de Veículos"])
app.include_router(veiculo, prefix="/veiculos", tags=["Veículos"])
app.include_router(motorista_veiculo, prefix="/vinculos", tags=["Motorista/Veículo"])
app.include_router(servico, prefix="/servicos", tags=["Serviços"])
app.include_router(avaliacao, prefix="/avaliacao", tags=["Avaliações"])
app.include_router(metodo_pagamento, prefix="/metodo-pagamento", tags=["Métodos de Pagamento"])
app.include_router(pagamento, prefix="/pagamento", tags=["Pagamentos"])
app.include_router(corrida, prefix="/corrida", tags=["Corridas"])


@app.get("/")
async def health_check():
    return {"status": "API Online"}