from pydantic import BaseModel, ConfigDict
from datetime import datetime
from decimal import Decimal
from typing import Optional
from enum import Enum

class StatusCorridaEnum(str, Enum):
    pendente = "Pendente"
    em_andamento = "Em andamento"
    concluida = "Concluída"
    cancelada = "Cancelada"

class CorridaSchema(BaseModel):
    id_passageiro: int
    id_motorista: Optional[int] = None
    id_servico: int
    id_avaliacao: Optional[int] = None
    datahora_inicio: datetime
    datahora_fim: Optional[datetime] = None
    local_partida: str
    local_destino: str
    valor_estimado: Decimal
    status: StatusCorridaEnum

    model_config = ConfigDict(from_attributes=True)

class CorridaUpdateSchema(BaseModel):
    id_motorista: Optional[int] = None
    datahora_fim: Optional[datetime] = None
    status: Optional[StatusCorridaEnum] = None