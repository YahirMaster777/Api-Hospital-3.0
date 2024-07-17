from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.roles, config.db, schemas.roles, models.roles
from typing import List

rol = APIRouter()
models.roles.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
    
# @rol.get("/roles/",  response_model=List[schemas.roles.Roles], tags=['Roles'])
# def read_roles(skip: int = 0,limit: int = 10,db: Session = Depends(get_db)):
#     db_roles = crud.roles.get_roles(db=db,skip=skip,limit=limit)
#     return db_roles

@rol.get("/roles/", response_model=List[schemas.roles.Roles],tags=['Roles'])
def read_roles(skip:int=0, limit:int=10, db:Session=Depends(get_db)):
    db_rol = crud.roles.get_allroles(skip=skip, limit=limit,db=db,)
    return db_rol

@rol.post("/roles/", response_model=schemas.roles.Roles, tags=["Roles"])
def create_rol(rol:schemas.roles.RolesCreate, db:Session= Depends(get_db)):
    db_rol = crud.roles.get_rol_byID(db,id=id)
    
    if db_rol:
        raise  HTTPException(status_code=400, detail="El rol, ya existe")
    return crud.roles.create_role(db=db, roles=rol)


@rol.get("/'roles'/{id}/", response_model=schemas.roles.Roles, tags=["Roles"])
def read_rol (id:int, db:Session= Depends(get_db)):
    db_rol = crud.roles.get_rol_byID(db=db, id=id)
    if db_rol is None:
        raise HTTPException(status_code= 404, detail="Rol no encontrado")
    return db_rol

@rol.put("/rolesput/{id}/", response_model=schemas.roles.Roles, tags=["Roles"])
def update_rol(id: int, role_update: schemas.roles.RolesUpdate, db: Session= Depends(get_db)):
    db_rol = crud.roles.update_rol(db=db, id=id,role_update=role_update)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="El nacimiento no existe")
    return db_rol
    

@rol.delete("/rolesdelete/{id}", response_model=schemas.roles.Roles, tags=["Roles"])
def delete_roles(id: int, db: Session = Depends(get_db)):
    db_rol = crud.roles.delete_rol(db=db, id=id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="El nacimiento no existe, no se pudo eliminar")
    return db_rol

