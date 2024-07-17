from typing import Optional
from fastapi import APIRouter, HTTPException
from datetime import datetime
from pydantic import BaseModel

persona_router = APIRouter()
personas = []


class ListarPersonas(BaseModel):
     id: str
     nombre: str
     primer_apellido: str
     segundo_apellido: Optional[str] = None
     edad: int
     fecha_nacimiento: datetime
     curp: str
     tipo_sangre: str
     fecha_creacion: datetime = datetime.now()
     estatus: bool = False


@persona_router.get("/personas")
def get_personas():
     return personas

@persona_router.post("/personas")
def enviar_datos(guardar_personas: ListarPersonas):
     personas.append(guardar_personas.dict())
     return {"message": "Datos Enviados"}


@persona_router.put("/personas/{id}")
def update_persona(id: str, update_persona: ListarPersonas):
     global personas
     index = next((i for i, persona in enumerate(
          personas) if persona["id"] == id), None)
     if index is None:
          raise HTTPException(
               status_code=404, detail="el id de la Persona no existe")
     personas[index] = update_persona.dict()
     return {"message": "Datos Actualizados"}


@persona_router.get("/personas/{id}")
def get_persona(id: str):
     persona = next(
          (persona for persona in personas if persona["id"] == id), None)
     if not persona:
          raise HTTPException(
               status_code=404, detail="el id de la Persona no existe")
     return persona


@persona_router.delete("/personas/{id}")
def delete_persona(id: str):
     global personas
     persona_to_delete = next(
          (persona for persona in personas if persona["id"] == id), None)
     if not persona_to_delete:
          raise HTTPException(
               status_code=404, detail="el id de la Persona no existe")
     personas = [persona for persona in personas if persona["id"] != id]
     return {"message": "Datos Eliminados"}
