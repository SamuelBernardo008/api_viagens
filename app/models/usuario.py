from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class UsuarioModel(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    cpf = Column(String(11), nullable=False, unique=True) 
    data_nascimento = Column(String(500), nullable=False)
    idade = Column(Integer, nullable=False)
    senha = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    nome_usuario = Column(String(255), nullable=False, unique=True)

    passageiro = relationship("PassageiroModel", back_populates="usuario_pai", uselist=False)
    motorista = relationship("MotoristaModel", back_populates="usuario_pai", uselist=False)