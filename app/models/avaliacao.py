from sqlalchemy import Column, Integer, SmallInteger, DateTime
from app.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class AvaliacaoModel(Base):
    __tablename__ = "avaliacoes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nota_passageiro = Column(SmallInteger, nullable=True) 
    nota_motorista = Column(SmallInteger, nullable=True)  
    datahora_limite = Column(DateTime, default=datetime.utcnow)
    
    corrida = relationship("CorridaModel", back_populates="avaliacao")