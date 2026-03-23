from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.motorista import MotoristaModel
from app.schema.motorista import MotoristaSchema, MotoristaUpdateSchema
from app.models.usuario import UsuarioModel

motorista = APIRouter(tags=["Motoristas"])

@motorista.post("/Criar")
async def criar_motorista(dados: MotoristaSchema, db: Session = Depends(get_db)):
    usuario_existe = db.query(UsuarioModel).filter(UsuarioModel.id == dados.usuario_id).first()
    
    if not usuario_existe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Usuário com ID {dados.usuario_id} não encontrado. Não é possível criar o motorista."
        )
    
    motorista_duplicado = db.query(MotoristaModel).filter(MotoristaModel.usuario_id == dados.usuario_id).first()
    if motorista_duplicado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Este usuário já possui um perfil de motorista ativo."
        )

    novo_motorista = MotoristaModel(**dados.model_dump())
    db.add(novo_motorista)
    db.commit()
    db.refresh(novo_motorista)
    return novo_motorista

@motorista.get("/Listar")
async def listar_motoristas(db: Session = Depends(get_db)):
    return db.query(MotoristaModel).all()

@motorista.get("/Buscar/{motorista_id}")
async def buscar_motorista(motorista_id: int, db: Session = Depends(get_db)):
    # Faz a consulta no banco de dados pelo ID
    motorista_api = db.query(MotoristaModel).filter(MotoristaModel.id == motorista_id).first()

    # Se não encontrar, retorna o erro 404
    if not motorista_api:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Motorista com ID {motorista_id} não encontrado."
        )

    return motorista_api


@motorista.put("/Atualizar/{motorista_id}")
async def atualizar_motorista(motorista_id: int, dados: MotoristaUpdateSchema, db: Session = Depends(get_db)):
    motorista_api = db.query(MotoristaModel).filter(MotoristaModel.id == motorista_id).first()

    if not motorista_api:
        raise HTTPException(status_code=404, detail="Motorista não encontrado")
    
    for chave, valor in dados.model_dump().items():
        setattr(motorista_api, chave, valor)

    db.add(motorista_api)
    db.commit()
    db.refresh(motorista_api) 

    return {"message": "Motorista atualizado com sucesso", "Motorista": motorista_api}

@motorista.delete("/Apagar/{motorista_id}")
async def deletar_motorista(motorista_id: int, db: Session = Depends(get_db)):
    motorista_api = db.query(MotoristaModel).filter(MotoristaModel.id == motorista_id).first()

    if not motorista_api:
        raise HTTPException(status_code=404, detail="Motorista não encontrado")

    db.delete(motorista_api)
    db.commit()
    return {"message": "Motorista removido com sucesso"}