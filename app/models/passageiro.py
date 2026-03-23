from sqlalchemy import Column, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from app.database import Base

class PassageiroModel(Base):
    __tablename__ = "passageiro"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    media_avaliacao = Column(Float, nullable=True)

    usuario_pai = relationship("UsuarioModel", back_populates="passageiro")
    corrida = relationship("CorridaModel", back_populates="passageiro")
