from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.veiculo import VeiculoModel
from app.schema.veiculo import VeiculoSchema, VeiculoUpdateSchema 
from app.models.modelo_veiculo import ModeloVeiculoModel 

veiculo = APIRouter(tags=["Veículos"])

@veiculo.post("/criarVeiculo")
async def criar_veiculo(dados: VeiculoSchema, db: Session = Depends(get_db)):
    modelo_existe = db.query(ModeloVeiculoModel).filter(ModeloVeiculoModel.id == dados.id_modelo).first()
    if not modelo_existe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Modelo com ID {dados.id_modelo} não encontrado."
        )
    
    placa_duplicada = db.query(VeiculoModel).filter(VeiculoModel.placa == dados.placa).first()
    if placa_duplicada:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Já existe um veículo cadastrado com esta placa."
        )

    novo_veiculo = VeiculoModel(**dados.model_dump())
    db.add(novo_veiculo)
    db.commit()
    db.refresh(novo_veiculo)
    return novo_veiculo

@veiculo.get("/veiculos")
async def listar_veiculos(db: Session = Depends(get_db)):
    return db.query(VeiculoModel).all()

@veiculo.put("/updateVeiculo/{veiculo_id}")
async def atualizar_veiculo(veiculo_id: int, dados: VeiculoUpdateSchema, db: Session = Depends(get_db)):
    veiculo_db = db.query(VeiculoModel).filter(VeiculoModel.id == veiculo_id).first()

    if not veiculo_db:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    
    dados_dict = dados.model_dump(exclude_unset=True)
    for chave, valor in dados_dict.items():
        setattr(veiculo_db, chave, valor)

    db.commit()
    db.refresh(veiculo_db) 

    return {"message": "Veículo atualizado com sucesso", "veiculo": veiculo_db}

@veiculo.delete("/deleteVeiculo/{veiculo_id}")
async def deletar_veiculo(veiculo_id: int, db: Session = Depends(get_db)):
    veiculo_db = db.query(VeiculoModel).filter(VeiculoModel.id == veiculo_id).first()

    if not veiculo_db:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")

    db.delete(veiculo_db)
    db.commit()
    return {"message": "Veículo removido com sucesso"}