import models.roles
import schemas.roles
from sqlalchemy.orm import Session

def create_role(db: Session, roles: schemas.roles.Roles):
    db_rol = models.roles.Roles(**roles.dict())
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol    

def get_roles(db:Session, id: int):
    return db.query(models.roles.Roles).filter(models.roles.Roles.id == id).all()

def get_rol_byID(db:Session, id: int):
    return db.query(models.roles.Roles).filter(
        models.roles.Roles.id == id).first()

def get_allroles(db:Session, skip: int = 0, limit: int = 10):
    return db.query(models.roles.Roles).offset(skip).limit(limit).all()



    
def update_rol(db: Session, id: int, role_update: schemas.roles.RolesUpdate):
    db_rol = db.query(models.roles.Roles).filter(models.roles.Roles.id == id).first()
    if db_rol:
        for key, value in role_update.dict(exclude_unset=True).items():
            setattr(db_rol, key, value)
        db.commit()
        db.refresh(db_rol)
        return db_rol
    return None


def delete_rol(db: Session, id: int):
    db_rol = db.query(models.roles.Roles).filter(models.roles.Roles.id == id).first()
    if db_rol:
        db.delete(db_rol)
        db.commit()
    return db_rol


