from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class PropriedadeEnum(enum.Enum):
    alugado = "alugado"
    proprio = "proprio"

class ModeloVeiculoModel(Base):
    __tablename__ = "modelo_veiculo"

    id = Column(Integer, primary_key=True, index=True)
    nome_modelo = Column(String(50), nullable=False)
    cor = Column(String(20), nullable=False)
    fabricante = Column(String(30), nullable=False)
    ano = Column(Integer, nullable=False)
    capacidade = Column(Integer, nullable=False)
    propriedade = Column(Enum(PropriedadeEnum), nullable=False)
    id_combustivel = Column(Integer, ForeignKey("combustivel.id"), nullable=False)

    combustivel = relationship("CombustivelModel", back_populates="modelo_veiculo")
