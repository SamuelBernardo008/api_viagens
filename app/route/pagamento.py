from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.pagamento import PagamentoModel
from app.schema.pagamento import PagamentoSchema, PagamentoUpdateSchema

pagamento = APIRouter(tags=["Pagamentos"])

@pagamento.post("/Criar", response_model=PagamentoSchema, status_code=status.HTTP_201_CREATED)
async def criar_pagamento(dados: PagamentoSchema, db: Session = Depends(get_db)):
    # Aqui você poderia validar se a corrida existe antes de criar o pagamento
    novo_pagamento = PagamentoModel(**dados.model_dump())
    db.add(novo_pagamento)
    db.commit()
    db.refresh(novo_pagamento)
    return novo_pagamento

@pagamento.get("/Listar")
async def listar_pagamentos(db: Session = Depends(get_db)):
    return db.query(PagamentoModel).all()

@pagamento.get("/Buscar/{id_pagamento}")
async def buscar_pagamento(id_pagamento: int, db: Session = Depends(get_db)):
    res = db.query(PagamentoModel).filter(PagamentoModel.id_pagamento == id_pagamento).first()
    if not res:
        raise HTTPException(status_code=404, detail="Pagamento não encontrado")
    return res

@pagamento.put("/Atualizar/{id_pagamento}")
async def atualizar_pagamento(id_pagamento: int, dados: PagamentoUpdateSchema, db: Session = Depends(get_db)):
    pagamento_db = db.query(PagamentoModel).filter(PagamentoModel.id_pagamento == id_pagamento).first()
    if not pagamento_db:
        raise HTTPException(status_code=404, detail="Pagamento não encontrado")
    
    for chave, valor in dados.model_dump(exclude_unset=True).items():
        setattr(pagamento_db, chave, valor)
    
    db.commit()
    db.refresh(pagamento_db)
    return pagamento_db

@pagamento.delete("/Apagar/{id_pagamento}")
async def apagar_pagamento(id_pagamento: int, db: Session = Depends(get_db)):
    pagamento_db = db.query(PagamentoModel).filter(PagamentoModel.id_pagamento == id_pagamento).first()
    if not pagamento_db:
        raise HTTPException(status_code=404, detail="Pagamento não encontrado")
    
    db.delete(pagamento_db)
    db.commit()
    return {"message": "Pagamento removido com sucesso"}