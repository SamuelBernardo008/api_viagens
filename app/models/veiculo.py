from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class VeiculoModel(Base):
    __tablename__ = "veiculo"

    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String(7), nullable=False, unique=True)
    id_modelo_veiculo = Column(Integer, ForeignKey("modelo_veiculo.id"), nullable=False)
    tem_seguro = Column(Boolean, nullable=False, default=False)
    id_classe = Column(Integer, ForeignKey("classe.id"), nullable=False)

    
    modelo = relationship("ModeloVeiculoModel", back_populates="veiculos")
    classe = relationship("ClasseModel", back_populates="veiculos")
    motorista_veiculo = relationship("MotoristaVeiculoModel", back_populates="veiculo")

