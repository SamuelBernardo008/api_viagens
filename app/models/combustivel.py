from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database import Base

class CombustivelModel(Base):
    __tablename__ = "combustivel"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(255), nullable=False)
    fator_carbono = Column(Float, nullable=True)

    
    modelo_veiculo = relationship("ModeloVeiculoModel", back_populates="combustivel")
