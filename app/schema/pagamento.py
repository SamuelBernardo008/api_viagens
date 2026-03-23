from pydantic import BaseModel, ConfigDict
from datetime import datetime
from decimal import Decimal
from typing import Optional

class PagamentoSchema(BaseModel):
    id_corrida: int
    valor: Decimal
    id_metodo_pagamento: int
    datahora_transacao: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

class PagamentoUpdateSchema(BaseModel):
    valor: Optional[Decimal] = None
    id_metodo_pagamento: Optional[int] = None