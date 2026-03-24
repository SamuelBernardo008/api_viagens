from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.avaliacao import AvaliacaoModel
from app.schema.avaliacao import AvaliacaoSchema, AvaliacaoUpdateSchema

avaliacao = APIRouter(tags=["Avaliações"])

@avaliacao.post("/Criar", response_model=AvaliacaoSchema)
async def criar_avaliacao(dados: AvaliacaoSchema, db: Session = Depends(get_db)):
    nova_avaliacao = AvaliacaoModel(**dados.model_dump())
    db.add(nova_avaliacao)
    db.commit()
    db.refresh(nova_avaliacao)
    return nova_avaliacao

@avaliacao.get("/Listar")
async def listar_avaliacoes(db: Session = Depends(get_db)):
    return db.query(AvaliacaoModel).all()

@avaliacao.get("/Buscar/{id_avaliacao}")
async def buscar_avaliacao(id_avaliacao: int, db: Session = Depends(get_db)):
    res = db.query(AvaliacaoModel).filter(AvaliacaoModel.id_avaliacao == id_avaliacao).first()
    if not res:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    return res

@avaliacao.put("/Atualizar/{id_avaliacao}")
async def atualizar_avaliacao(id_avaliacao: int, dados: AvaliacaoUpdateSchema, db: Session = Depends(get_db)):
    item_db = db.query(AvaliacaoModel).filter(AvaliacaoModel.id_avaliacao == id_avaliacao).first()
    if not item_db:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    
    for chave, valor in dados.model_dump(exclude_unset=True).items():
        setattr(item_db, chave, valor)
    
    db.commit()
    db.refresh(item_db)
    return item_db

@avaliacao.delete("/Apagar/{id_avaliacao}")
async def apagar_avaliacao(id_avaliacao: int, db: Session = Depends(get_db)):
    item_db = db.query(AvaliacaoModel).filter(AvaliacaoModel.id_avaliacao == id_avaliacao).first()
    if not item_db:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    
    db.delete(item_db)
    db.commit()
    return {"message": "Avaliação removida com sucesso"}