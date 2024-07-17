import models.roles_user
import schemas.roles_user
from sqlalchemy.orm import Session
import models, schemas

def get_role_user(db: Session, id_user: int, id_rol: int):
    return db.query(models.roles_user.UserRol).filter(models.roles_user.UserRol.Usuario_ID == id_user, models.roles_user.UserRol.Rol_ID== id_rol).first()

def get_roles_user(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.roles_user.UserRol).offset(skip).limit(limit).all()

def create_roles_user(db: Session, roles_user: schemas.roles_user.UserRolCreate):
    db_roles_user = models.roles_user.UserRol(Usuario_ID=roles_user.Usuario_ID, 
                                          Rol_ID = roles_user.Rol_ID,
                                          Estatus = roles_user.Estatus, 
                                          Fecha_Registro = roles_user.Fecha_Registro,
                                          Fecha_Actualizacion = roles_user.Fecha_Actualizacion 
                                )
    db.add(db_roles_user)
    db.commit()
    db.refresh(db_roles_user)
    return db_roles_user

def update_roles_user(db: Session, id_user: int, id_rol: int, roles_user: schemas.roles_user.UserRolUpdate):
    db_roles_user = db.query(models.roles_user.UserRol).filter(models.roles_user.UserRol.Usuario_ID == id_user,models.roles_user.UserRol.Rol_ID == id_rol).first()
    if db_roles_user:
        for var, value in vars(roles_user).items():
            setattr(db_roles_user, var, value) if value else None
        db.commit()
        db.refresh(db_roles_user)
    return db_roles_user

def delete_roles_user(db: Session, id_user: int, id_rol:int):
    db_roles_user = db.query(models.roles_user.UserRol).filter(models.roles_user.UserRol.Usuario_ID == id_user, models.roles_user.UserRol.Rol_ID== id_rol).first()
    if db_roles_user:
        db.delete(db_roles_user)
        db.commit()
    return db_roles_user