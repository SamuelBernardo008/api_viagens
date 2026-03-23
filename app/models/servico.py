from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class ServicoModel(Base):
    __tablename__ = "servico"

    id = Column(Integer, primary_key=True, index=True)
    nome_servico = Column(String(50), nullable=False)
    id_classe_minima = Column(Integer, ForeignKey("classe.id"), nullable=False)

    classe = relationship("ClasseModel", back_populates="servicos")
    corrida = relationship("CorridaModel", back_populates="servicos")
