from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario import UsuarioModel
from app.schema.usuario import UsuarioSchema, UsuarioUpdateSchema


usuario = APIRouter(tags=["Usuários"])

@usuario.post("/Criar")
async def criar_usuario(dados: UsuarioSchema, db: Session = Depends(get_db)):
    novo_usuario = UsuarioModel(**dados.model_dump())
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return {"message": "Usuário criado com sucesso", "usuario": novo_usuario}

@usuario.get("/Listar")
async def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(UsuarioModel).all()


@usuario.get("/Buscar/{usuario_id}")
async def buscar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    # Faz a busca no banco pelo ID fornecido na URL
    usuario_db = db.query(UsuarioModel).filter(UsuarioModel.id == usuario_id).first()

    # Verifica se o usuário existe
    if not usuario_db:
        raise HTTPException(
            status_code=404, 
            detail=f"Usuário com ID {usuario_id} não encontrado."
        )

    return usuario_db

@usuario.put("/Atualizar/{usuario_id}")
async def atualizar_usuario(usuario_id: int, dados: UsuarioUpdateSchema, db: Session = Depends(get_db)):
    usuario_api = db.query(UsuarioModel).filter(UsuarioModel.id == usuario_id).first()

    if not usuario_api:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    for chave, valor in dados.model_dump().items():
        setattr(usuario_api, chave, valor)

    db.add(usuario_api)
    db.commit()
    db.refresh(usuario_api) 

    return {"message": "Usuário atualizado com sucesso", "usuario": usuario_api}

@usuario.delete("/Apagar/{usuario_id}")
async def deletar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario_api = db.query(UsuarioModel).filter(UsuarioModel.id == usuario_id).first()

    if not usuario_api:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    db.delete(usuario_api)
    db.commit()
    return {"message": "Usuário removido com sucesso"}