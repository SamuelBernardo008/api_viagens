from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.classe import ClasseModel
from app.schema.classe import ClasseSchema, ClasseUpdateSchema

classe = APIRouter(tags=["Classes de Veículos"])

@classe.post("/criar", response_model=ClasseSchema, status_code=status.HTTP_201_CREATED)
async def criar_classe(dados: ClasseSchema, db: Session = Depends(get_db)):
    # Validação para evitar classes com nomes idênticos
    classe_existe = db.query(ClasseModel).filter(ClasseModel.nome_classe == dados.nome_classe).first()
    if classe_existe:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"A classe '{dados.nome_classe}' já existe."
        )

    nova_classe = ClasseModel(**dados.model_dump())
    db.add(nova_classe)
    db.commit()
    db.refresh(nova_classe)
    return nova_classe

@classe.get("/listar")
async def listar_classes(db: Session = Depends(get_db)):
    return db.query(ClasseModel).all()

@classe.get("/buscar/{classe_id}")
async def buscar_classe(classe_id: int, db: Session = Depends(get_db)):
    classe_db = db.query(ClasseModel).filter(ClasseModel.id == classe_id).first()
    if not classe_db:
        raise HTTPException(status_code=404, detail="Classe não encontrada")
    return classe_db

@classe.put("/atualizar/{classe_id}")
async def atualizar_classe(classe_id: int, dados: ClasseUpdateSchema, db: Session = Depends(get_db)):
    classe_db = db.query(ClasseModel).filter(ClasseModel.id == classe_id).first()

    if not classe_db:
        raise HTTPException(status_code=404, detail="Classe não encontrada")
    
    # Atualiza apenas os campos enviados (exclude_unset=True)
    dados_dict = dados.model_dump(exclude_unset=True)
    for chave, valor in dados_dict.items():
        setattr(classe_db, chave, valor)

    db.commit()
    db.refresh(classe_db) 

    return {"message": "Classe atualizada com sucesso", "classe": classe_db}

@classe.delete("/apagar/{classe_id}")
async def deletar_classe(classe_id: int, db: Session = Depends(get_db)):
    classe_db = db.query(ClasseModel).filter(ClasseModel.id == classe_id).first()

    if not classe_db:
        raise HTTPException(status_code=404, detail="Classe não encontrada")

    # Nota: Se houver veículos vinculados a esta classe, o banco pode impedir a deleção
    # dependendo da sua configuração de FK (Foreign Key).
    try:
        db.delete(classe_db)
        db.commit()
    except Exception:
        raise HTTPException(
            status_code=400, 
            detail="Não é possível excluir uma classe que possui veículos vinculados."
        )
        
    return {"message": "Classe removida com sucesso"}