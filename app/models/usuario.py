import string

from sqlalchemy import Column, Integer, String
from app.database import Base

class UsuarioModel(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    cpf = Column(String(11), nullable=False, unique=True) #integer é muito pequeno para um usuario com um cpf de 11 digitos ent tem que ser string.
    data_nascimento = Column(String(500), nullable=False)
    idade = Column(Integer, nullable=False)
    senha = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    nome_usuario = Column(String(255), nullable=False, unique=True)
