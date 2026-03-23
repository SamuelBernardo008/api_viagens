from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.modelo_veiculo import ModeloVeiculoModel
from app.models.combustivel import CombustivelModel 
from app.schema.modelo_veiculo import ModeloVeiculoSchema, ModeloVeiculoUpdateSchema

modelo_veiculo = APIRouter(tags=["Modelos de Veículos"])

@modelo_veiculo.post("/Criar", status_code=status.HTTP_201_CREATED)
async def criar_modelo(dados: ModeloVeiculoSchema, db: Session = Depends(get_db)):
    combustivel = db.query(CombustivelModel).filter(CombustivelModel.id == dados.id_combustivel).first()
    if not combustivel:
        raise HTTPException(
            status_code=404, 
            detail=f"Combustível com ID {dados.id_combustivel} não encontrado."
        )

    novo_modelo = ModeloVeiculoModel(**dados.model_dump())
    db.add(novo_modelo)
    db.commit()
    db.refresh(novo_modelo)
    return {"message": "Modelo de veículo criado com sucesso", "modelo": novo_modelo}

@modelo_veiculo.get("/Listar")
async def listar_modelos(db: Session = Depends(get_db)):
    return db.query(ModeloVeiculoModel).all()

@modelo_veiculo.get("/Buscar/{modelo_id}")
async def buscar_modelo(modelo_id: int, db: Session = Depends(get_db)):
    modelo = db.query(ModeloVeiculoModel).filter(ModeloVeiculoModel.id == modelo_id).first()
    if not modelo:
        raise HTTPException(status_code=404, detail="Modelo não encontrado")
    return modelo

@modelo_veiculo.put("/Atualizar/{modelo_id}")
async def atualizar_modelo(modelo_id: int, dados: ModeloVeiculoUpdateSchema, db: Session = Depends(get_db)):
    modelo_db = db.query(ModeloVeiculoModel).filter(ModeloVeiculoModel.id == modelo_id).first()

    if not modelo_db:
        raise HTTPException(status_code=404, detail="Modelo não encontrado")
    
    dados_dict = dados.model_dump(exclude_unset=True)
    
    for chave, valor in dados_dict.items():
        setattr(modelo_db, chave, valor)

    db.commit()
    db.refresh(modelo_db)
    return {"message": "Modelo atualizado com sucesso", "modelo": modelo_db}

@modelo_veiculo.delete("/Apgar/{modelo_id}")
async def deletar_modelo(modelo_id: int, db: Session = Depends(get_db)):
    modelo_db = db.query(ModeloVeiculoModel).filter(ModeloVeiculoModel.id == modelo_id).first()

    if not modelo_db:
        raise HTTPException(status_code=404, detail="Modelo não encontrado")

    try:
        db.delete(modelo_db)
        db.commit()
    except Exception:
        # LÓGICA: Se houver um erro, provavelmente é porque existem Veículos vinculados a este modelo (FK)
        db.rollback()
        raise HTTPException(
            status_code=400, 
            detail="Não é possível remover este modelo pois existem veículos vinculados a ele."
        )
        
    return {"message": "Modelo removido com sucesso"}