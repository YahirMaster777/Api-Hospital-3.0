from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, Date
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base


class Roles(Base):  
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(50),nullable=False)
    Description = Column(LONGTEXT, nullable=False)
    Estatus = Column(Boolean, nullable=False)
    Fecha_Registro= Column(Date)
    Fecha_Actualizacion = Column(DateTime)
