from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.passageiro import PassageiroModel
from app.schema.passageiro import PassageiroSchema, PassageiroUpdateSchema
from app.models.usuario import UsuarioModel

passageiro = APIRouter(tags=["Passageiros"])

@passageiro.post("/criarPassageiro")
async def criar_passageiro(dados: PassageiroSchema, db: Session = Depends(get_db)):
    usuario_existe = db.query(UsuarioModel).filter(UsuarioModel.id == dados.usuario_id).first()
    
    if not usuario_existe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Usuário com ID {dados.usuario_id} não encontrado. Não é possível criar o passageiro."
        )
    
    passageiro_duplicado = db.query(PassageiroModel).filter(PassageiroModel.usuario_id == dados.usuario_id).first()
    if passageiro_duplicado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Este usuário já possui um perfil de passageiro ativo."
        )

    novo_passageiro = PassageiroModel(**dados.model_dump())
    db.add(novo_passageiro)
    db.commit()
    db.refresh(novo_passageiro)
    return novo_passageiro

@passageiro.get("/passageiros")
async def listar_passageiros(db: Session = Depends(get_db)):
    return db.query(PassageiroModel).all()


@passageiro.put("/updatePassageiro/{passageiro_id}")
async def atualizar_passageiro(passageiro_id: int, dados: PassageiroUpdateSchema, db: Session = Depends(get_db)):
    passageiro_api = db.query(PassageiroModel).filter(PassageiroModel.id == passageiro_id).first()

    if not passageiro_api:
        raise HTTPException(status_code=404, detail="Passageiro não encontrado")
    
    for chave, valor in dados.model_dump().items():
        setattr(passageiro_api, chave, valor)

    db.add(passageiro_api)
    db.commit()
    db.refresh(passageiro_api) 

    return {"message": "Passageiro atualizado com sucesso", "Passageiro": passageiro_api}

@passageiro.delete("/deletePassageiro/{passageiro_id}")
async def deletar_passageiro(passageiro_id: int, db: Session = Depends(get_db)):
    passageiro_api = db.query(PassageiroModel).filter(PassageiroModel.id == passageiro_id).first()

    if not passageiro_api:
        raise HTTPException(status_code=404, detail="Passageiro não encontrado")

    db.delete(passageiro_api)
    db.commit()
    return {"message": "Passageiro removido com sucesso"}