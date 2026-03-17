from typing import Optional

from pydantic import BaseModel

class PassageiroSchema(BaseModel):
    usuario_id: int
    media_avaliacao: float

    class config:
        from_attributes = True
        

class PassageiroUpdateSchema(BaseModel):
    media_avaliacao: Optional[float] = None

    class config:
        from_attributes = True
