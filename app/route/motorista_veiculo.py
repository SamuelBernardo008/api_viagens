from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.motorista_veiculo import MotoristaVeiculoModel
from app.models.veiculo import VeiculoModel
from app.models.motorista import MotoristaModel 
from app.schema.motorista_veiculo import MotoristaVeiculoSchema, MotoristaVeiculoUpdateSchema

motorista_veiculo = APIRouter(tags=["Motorista/Veículo"])

@motorista_veiculo.post("/Criar")
async def vincular_motorista(dados: MotoristaVeiculoSchema, db: Session = Depends(get_db)):
    # 1. Valida se o Motorista existe
    motorista = db.query(MotoristaModel).filter(MotoristaModel.id == dados.id_motorista).first()
    if not motorista:
        raise HTTPException(status_code=404, detail="Motorista não encontrado.")

    # 2. Valida se o Veículo existe
    veiculo = db.query(VeiculoModel).filter(VeiculoModel.id == dados.id_veiculo).first()
    if not veiculo:
        raise HTTPException(status_code=404, detail="Veículo não encontrado.")

    # 3. Lógica extra (Opcional): Verificar se o veículo já está em uso (sem data_fim)
    uso_atual = db.query(MotoristaVeiculoModel).filter(
        MotoristaVeiculoModel.id_veiculo == dados.id_veiculo,
        MotoristaVeiculoModel.datahora_fim == None
    ).first()
    
    if uso_atual:
        raise HTTPException(
            status_code=400, 
            detail=f"Este veículo já está sendo utilizado pelo motorista ID {uso_atual.id_motorista}"
        )

    novo_vinculo = MotoristaVeiculoModel(**dados.model_dump())
    db.add(novo_vinculo)
    db.commit()
    db.refresh(novo_vinculo)
    return novo_vinculo

@motorista_veiculo.get("/Listar")
async def listar_vinculos(db: Session = Depends(get_db)):
    return db.query(MotoristaVeiculoModel).all()

@motorista_veiculo.put("/Atualizar/{vinculo_id}")
async def atualizar_vinculo(vinculo_id: int, dados: MotoristaVeiculoUpdateSchema, db: Session = Depends(get_db)):
    vinculo_db = db.query(MotoristaVeiculoModel).filter(MotoristaVeiculoModel.id == vinculo_id).first()

    if not vinculo_db:
        raise HTTPException(status_code=404, detail="Vínculo não encontrado")
    
    dados_dict = dados.model_dump(exclude_unset=True)
    for chave, valor in dados_dict.items():
        setattr(vinculo_db, chave, valor)

    db.commit()
    db.refresh(vinculo_db)
    return {"message": "Vínculo atualizado com sucesso", "vinculo": vinculo_db}

@motorista_veiculo.delete("/Apagar/{vinculo_id}")
async def remover_vinculo(vinculo_id: int, db: Session = Depends(get_db)):
    vinculo_db = db.query(MotoristaVeiculoModel).filter(MotoristaVeiculoModel.id == vinculo_id).first()

    if not vinculo_db:
        raise HTTPException(status_code=404, detail="Vínculo não encontrado")

    db.delete(vinculo_db)
    db.commit()
    return {"message": "Vínculo removido com sucesso"}