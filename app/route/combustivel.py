from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.combustivel import CombustivelModel
from app.schema.combustivel import CombustivelSchema, CombustivelUpdateSchema

combustivel = APIRouter(tags=["Combustíveis"])

@combustivel.post("/Criar", status_code=status.HTTP_201_CREATED)
async def criar_combustivel(dados: CombustivelSchema, db: Session = Depends(get_db)):
    # Opcional: Validar se já existe um combustível com a mesma descrição
    existente = db.query(CombustivelModel).filter(CombustivelModel.descricao == dados.descricao).first()
    if existente:
        raise HTTPException(
            status_code=400, 
            detail="Este tipo de combustível já está cadastrado."
        )

    novo_combustivel = CombustivelModel(**dados.model_dump())
    db.add(novo_combustivel)
    db.commit()
    db.refresh(novo_combustivel)
    return {"message": "Combustível cadastrado com sucesso", "combustivel": novo_combustivel}

@combustivel.get("/Listar")
async def listar_combustiveis(db: Session = Depends(get_db)):
    return db.query(CombustivelModel).all()

@combustivel.get("/Bucar/{combustivel_id}")
async def buscar_combustivel(combustivel_id: int, db: Session = Depends(get_db)):
    item = db.query(CombustivelModel).filter(CombustivelModel.id == combustivel_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Combustível não encontrado")
    return item

@combustivel.put("/Atualizar/{combustivel_id}")
async def atualizar_combustivel(combustivel_id: int, dados: CombustivelUpdateSchema, db: Session = Depends(get_db)):
    combustivel_db = db.query(CombustivelModel).filter(CombustivelModel.id == combustivel_id).first()

    if not combustivel_db:
        raise HTTPException(status_code=404, detail="Combustível não encontrado")
    
    # Atualiza apenas os campos enviados (exclude_unset=True)
    dados_dict = dados.model_dump(exclude_unset=True)
    for chave, valor in dados_dict.items():
        setattr(combustivel_db, chave, valor)

    db.commit()
    db.refresh(combustivel_db)
    return {"message": "Combustível atualizado com sucesso", "combustivel": combustivel_db}

@combustivel.delete("/Apagar/{combustivel_id}")
async def deletar_combustivel(combustivel_id: int, db: Session = Depends(get_db)):
    combustivel_db = db.query(CombustivelModel).filter(CombustivelModel.id == combustivel_id).first()

    if not combustivel_db:
        raise HTTPException(status_code=404, detail="Combustível não encontrado")

    try:
        db.delete(combustivel_db)
        db.commit()
    except Exception:
        # Erro comum: tentativa de deletar combustível que está sendo usado por um Modelo de Veículo
        db.rollback()
        raise HTTPException(
            status_code=400, 
            detail="Não é possível remover este combustível pois existem modelos de veículos vinculados a ele."
        )
        
    return {"message": "Combustível removido com sucesso"}