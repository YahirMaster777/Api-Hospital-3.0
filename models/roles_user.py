from sqlalchemy import Column, Integer,Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
import models.roles, models.users

class UserRol(Base):
    __tablename__ = "tbd_usuarios_roles"

    Usuario_ID = Column(Integer, ForeignKey("tbb_usuarios.ID"), primary_key=True)
    Rol_ID = Column(Integer, ForeignKey("roles.id"), primary_key=True)
    Estatus = Column(Boolean)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    