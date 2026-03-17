from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class MotoristaVeiculoModel(Base):
    __tablename__ = "motorista_veiculo"

    id = Column(Integer, primary_key=True, index=True)
    id_motorista = Column(Integer, ForeignKey("motorista.id"), nullable=False)
    id_veiculo = Column(Integer, ForeignKey("veiculo.id"), nullable=False)
    datahora_inicio = Column(DateTime, default=datetime.now, nullable=False)
    datahora_fim = Column(DateTime, nullable=True)
    
    motorista = relationship("MotoristaModel", back_populates="motorista_veiculo")
    veiculo = relationship("VeiculoModel", back_populates="motorista_veiculo")
