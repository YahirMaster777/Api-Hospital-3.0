from pydantic import BaseModel
from datetime import date

class RolesBase(BaseModel):
    Nombre : str
    Description: str
    Estatus: int
    Fecha_Registro: date
    Fecha_Actualizacion:date


class RolesCreate(RolesBase):
    pass

class RolesUpdate(RolesBase):
    pass

class Roles(RolesBase):
    id: int
    class Config:
        orm_mode = True
        
        