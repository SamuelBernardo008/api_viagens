from sqlalchemy import Column, BigInteger, SmallInteger, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class PagamentoModel(Base):
    __tablename__ = "pagamentos"

    id_pagamento = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    id_corrida = Column(BigInteger, ForeignKey("corridas.id"), nullable=False)
    valor = Column(Numeric(10, 2), nullable=False)
    id_metodo_pagamento = Column(SmallInteger, ForeignKey("metodos_pagamento.id"), nullable=False)
    datahora_transacao = Column(DateTime, default=datetime.utcnow)

    metodo = relationship("MetodoPagamentoModel", back_populates="pagamentos")
    corrida = relationship("CorridaModel", back_populates="pagamentos")