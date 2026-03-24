from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.corrida import CorridaModel
from app.schema.corrida import CorridaSchema, CorridaUpdateSchema

corrida = APIRouter(tags=["Corridas"])

@corrida.post("/Criar", response_model=CorridaSchema)
async def criar_corrida(dados: CorridaSchema, db: Session = Depends(get_db)):
    nova_corrida = CorridaModel(**dados.model_dump())
    db.add(nova_corrida)
    db.commit()
    db.refresh(nova_corrida)
    return nova_corrida

@corrida.get("/Listar")
async def listar_corridas(db: Session = Depends(get_db)):
    return db.query(CorridaModel).all()

@corrida.get("/Buscar/{id_corrida}")
async def buscar_corrida(id_corrida: int, db: Session = Depends(get_db)):
    corrida = db.query(CorridaModel).filter(CorridaModel.id == id_corrida).first()
    if not corrida:
        raise HTTPException(status_code=404, detail="Corrida não encontrada")
    return corrida

@corrida.put("/Atualizar/{id_corrida}")
async def atualizar_corrida(id_corrida: int, dados: CorridaUpdateSchema, db: Session = Depends(get_db)):
    corrida_db = db.query(CorridaModel).filter(CorridaModel.id == id_corrida).first()
    if not corrida_db:
        raise HTTPException(status_code=404, detail="Corrida não encontrada")
    
    for chave, valor in dados.model_dump(exclude_unset=True).items():
        setattr(corrida_db, chave, valor)
    
    db.commit()
    db.refresh(corrida_db)
    return corrida_db

@corrida.delete("/Apagar/{id_corrida}")
async def apagar_corrida(id_corrida: int, db: Session = Depends(get_db)):
    corrida_db = db.query(CorridaModel).filter(CorridaModel.id == id_corrida).first()
    if not corrida_db:
        raise HTTPException(status_code=404, detail="Corrida não encontrada")
    
    db.delete(corrida_db)
    db.commit()
    return {"message": "Corrida removida com sucesso"}