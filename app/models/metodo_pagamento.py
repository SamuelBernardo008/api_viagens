from sqlalchemy import Column, SmallInteger, String
from sqlalchemy.orm import relationship
from app.database import Base

class MetodoPagamentoModel(Base):
    __tablename__ = "metodos_pagamento"

    id = Column(SmallInteger, primary_key=True, index=True, autoincrement=True)
    descricao = Column(String(45), nullable=False)
    nome_financiera = Column(String(45), nullable=False)
    
    pagamentos = relationship("PagamentoModel", back_populates="metodo")