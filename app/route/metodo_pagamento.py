from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.metodo_pagamento import MetodoPagamentoModel
from app.schema.metodo_pagamento import MetodoPagamentoSchema, MetodoPagamentoUpdateSchema

metodo_pagamento = APIRouter(tags=["Métodos de Pagamento"])

@metodo_pagamento.post("/Criar", response_model=MetodoPagamentoSchema)
async def criar_metodo(dados: MetodoPagamentoSchema, db: Session = Depends(get_db)):
    novo_metodo = MetodoPagamentoModel(**dados.model_dump())
    db.add(novo_metodo)
    db.commit()
    db.refresh(novo_metodo)
    return novo_metodo

@metodo_pagamento.get("/Listar")
async def listar_metodos(db: Session = Depends(get_db)):
    return db.query(MetodoPagamentoModel).all()

@metodo_pagamento.get("/Buscar/{id_metodo}")
async def buscar_metodo(id_metodo: int, db: Session = Depends(get_db)):
    metodo = db.query(MetodoPagamentoModel).filter(MetodoPagamentoModel.id_metodo_pagamento == id_metodo).first()
    if not metodo:
        raise HTTPException(status_code=404, detail="Método de pagamento não encontrado")
    return metodo

@metodo_pagamento.put("/Atualizar/{id_metodo}")
async def atualizar_metodo(id_metodo: int, dados: MetodoPagamentoUpdateSchema, db: Session = Depends(get_db)):
    metodo_db = db.query(MetodoPagamentoModel).filter(MetodoPagamentoModel.id_metodo_pagamento == id_metodo).first()
    if not metodo_db:
        raise HTTPException(status_code=404, detail="Método de pagamento não encontrado")
    
    for chave, valor in dados.model_dump(exclude_unset=True).items():
        setattr(metodo_db, chave, valor)
    
    db.commit()
    db.refresh(metodo_db)
    return metodo_db

@metodo_pagamento.delete("/Apagar/{id_metodo}")
async def apagar_metodo(id_metodo: int, db: Session = Depends(get_db)):
    metodo_db = db.query(MetodoPagamentoModel).filter(MetodoPagamentoModel.id_metodo_pagamento == id_metodo).first()
    if not metodo_db:
        raise HTTPException(status_code=404, detail="Método de pagamento não encontrado")
    
    db.delete(metodo_db)
    db.commit()
    return {"message": "Método de pagamento removido com sucesso"}