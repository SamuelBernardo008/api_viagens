from sqlalchemy import Column, ForeignKey, Integer, Float, String
from sqlalchemy.orm import relationship
from app.database import Base

class MotoristaModel(Base):
    __tablename__ = "motorista"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    media_avaliacao = Column(Float, nullable=True)
    cnh = Column(String(9), nullable=False, unique=True)
    
    usuario_pai = relationship("UsuarioModel", back_populates="motorista")
