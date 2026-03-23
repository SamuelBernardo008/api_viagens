from typing import Optional

from pydantic import BaseModel

class VeiculoSchema(BaseModel):
    placa: str
    id_modelo_veiculo: int
    tem_seguro: bool
    id_classe: int

    class config:
        from_attributes = True
        

class VeiculoUpdateSchema(BaseModel):
    placa: Optional[str]
    tem_seguro: Optional[bool]


    class config:
        from_attributes = True
