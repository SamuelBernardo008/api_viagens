from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.servico import ServicoModel
from app.models.classe import ClasseModel
from app.schema.servico import ServicoSchema, ServicoUpdateSchema

servico = APIRouter(tags=["Serviços"])

@servico.post("/Criar", status_code=status.HTTP_201_CREATED)
async def criar_servico(dados: ServicoSchema, db: Session = Depends(get_db)):
    classe_existe = db.query(ClasseModel).filter(ClasseModel.id == dados.id_classe_minima).first()
    if not classe_existe:
        raise HTTPException(status_code=404, detail="Classe mínima não encontrada.")

    novo_servico = ServicoModel(**dados.model_dump())
    db.add(novo_servico)
    db.commit()
    db.refresh(novo_servico)
    return novo_servico

@servico.get("/Listar")
async def listar_servicos(db: Session = Depends(get_db)):
    return db.query(ServicoModel).all()

@servico.get("/Buscar{id_servico}")
async def buscar_servico(id_servico: int, db: Session = Depends(get_db)):
    servico_db = db.query(ServicoModel).filter(ServicoModel.id_servico == id_servico).first()
    if not servico_db:
        raise HTTPException(status_code=404, detail="Serviço não encontrado.")
    return servico_db

@servico.put("/Atualizar{id_servico}")
async def atualizar_servico(id_servico: int, dados: ServicoUpdateSchema, db: Session = Depends(get_db)):
    servico_db = db.query(ServicoModel).filter(ServicoModel.id_servico == id_servico).first()
    if not servico_db:
        raise HTTPException(status_code=404, detail="Serviço não encontrado.")

    for chave, valor in dados.model_dump(exclude_unset=True).items():
        setattr(servico_db, chave, valor)

    db.commit()
    db.refresh(servico_db)
    return servico_db

@servico.delete("/Apagar{id_servico}")
async def deletar_servico(id_servico: int, db: Session = Depends(get_db)):
    servico_db = db.query(ServicoModel).filter(ServicoModel.id_servico == id_servico).first()
    if not servico_db:
        raise HTTPException(status_code=404, detail="Serviço não encontrado.")
    
    db.delete(servico_db)
    db.commit()
    return {"message": "Serviço deletado com sucesso"}