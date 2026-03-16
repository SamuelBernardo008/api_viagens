from fastapi import FastAPI
from app.database import Base,engine
from app.route.usuario import usuario

Base.metadata.create_all(bind=engine)

app= FastAPI() #inicia a aplicação FastAPI

app.include_router(usuario)

@app.get("/")
async def health_check():
    return {"status": "API Online"}