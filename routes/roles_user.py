from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
import crud.roles_user
import crud.roles, config.db, schemas.roles_user, models.roles_user
from typing import List

roles_user = APIRouter()

models.roles_user.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@roles_user.get("/roles_user/", response_model=List[schemas.roles_user.UserRol], tags=["Usuarios Roles"])
def read_roles_user(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_roles_user= crud.roles_user.get_roles_user(db=db, skip=skip, limit=limit)
    return db_roles_user

@roles_user.post("/rol_user/{id_user}/{id_rol}", response_model=schemas.roles_user.UserRol, tags=["Usuarios Roles"])
def read_rol(id_user: int, id_rol: int, db: Session = Depends(get_db)):
    db_roles_user= crud.roles_user.get_role_user(db=db, id_user=id_user,id_rol=id_rol)

    if db_roles_user is None:
        raise HTTPException(status_code=404, detail="roles_user no existe")
    return db_roles_user



@roles_user.post("/rolescreate/", response_model=schemas.roles_user.UserRol, tags=["Usuarios Roles"])
def create_user(roles_user: schemas.roles_user.UserRolCreate, db: Session = Depends(get_db)):
    db_roles_user = crud.roles_user.get_roles_user(db=db, id_user=roles_user.Usuario_ID, id_rol=roles_user.Rol_ID)
    print (db_roles_user)
    if db_roles_user:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return crud.roles_user.create_roles_user(db=db, roles_user=roles_user)

@roles_user.put("/roleuserput/{id_user}/{id_rol}", response_model=schemas.roles_user.UserRol, tags=["Usuarios Roles"])
def update_user(id_user: int, id_rol: int, roles_user: schemas.roles_user.UserRolUpdate, db: Session = Depends(get_db)):
    db_roles_user = crud.roles_user.update_roles_user(db=db, id_user=id_user, id_rol=id_rol, roles_user=roles_user)
    print (db_roles_user.Estatus)
    if db_roles_user is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no actualizado")
    return db_roles_user

@roles_user.delete("/roles_user/{id_user}/{id_rol}", response_model=schemas.roles_user.UserRol, tags=["Usuarios Roles"])
def delete_rol(id_user: int, id_rol: int, db: Session = Depends(get_db)):
    db_roles_user = crud.roles_user.delete_roles_user(db=db, id_user=id_user, id_rol=id_rol)
    if db_roles_user is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no se pudo eliminar")
    return db_roles_user