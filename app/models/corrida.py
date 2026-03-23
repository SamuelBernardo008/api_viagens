from sqlalchemy import Column, BigInteger, Integer, String, DateTime, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class StatusCorrida(str, enum.Enum):
    pendente = "Pendente"
    em_andamento = "Em andamento"
    concluida = "Concluída"
    cancelada = "Cancelada"

class CorridaModel(Base):
    __tablename__ = "corridas"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    id_passageiro = Column(Integer, ForeignKey("passageiro.id"), nullable=False)
    id_motorista = Column(Integer, ForeignKey("motorista.id"), nullable=True) # Pode ser null se ainda não aceita
    id_servico = Column(Integer, ForeignKey("servico.id"), nullable=False)
    id_avaliacao = Column(Integer, ForeignKey("avaliacoes.id"), nullable=True)
    
    datahora_inicio = Column(DateTime, nullable=False)
    datahora_fim = Column(DateTime, nullable=True)
    local_partida = Column(String(50), nullable=False)
    local_destino = Column(String(50), nullable=False)
    valor_estimado = Column(Float, nullable=False)
    status = Column(Enum(StatusCorrida), default=StatusCorrida.pendente)
    
    passageiro = relationship("PassageiroModel", back_populates="corrida")
    motorista = relationship("MotoristaModel", back_populates="corrida")
    servicos = relationship("ServicoModel", back_populates="corrida")
    avaliacao = relationship("AvaliacaoModel", back_populates="corrida")
    pagamentos = relationship("PagamentoModel", back_populates="corrida")