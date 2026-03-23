from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database import Base

class ClasseModel(Base):
    __tablename__ = "classe"

    id = Column(Integer, primary_key=True, index=True)
    nome_classe = Column(String(255), nullable=False)
    fator_preco = Column(Float, nullable=False)

    
    veiculos = relationship("VeiculoModel", back_populates="classe")
    servicos = relationship("ServicoModel", back_populates="classe")