from typing import Optional

from pydantic import BaseModel

class MotoristaSchema(BaseModel):
    usuario_id: int
    media_avaliacao: float
    cnh: str

    class config:
        from_attributes = True
        

class MotoristaUpdateSchema(BaseModel):
    media_avaliacao: Optional[float] = None
    cnh: Optional[str]

    class config:
        from_attributes = True
