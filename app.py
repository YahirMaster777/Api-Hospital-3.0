from fastapi import FastAPI
from routes.personas import person
from routes.users import user
from routes.nacimientos import baby
from routes.roles import rol
from routes.roles_user import roles_user

from fastapi.middleware.cors import CORSMiddleware

#la api ya funciona para la tabla de nacimientos


app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(person, prefix="/api")
app.include_router(user, prefix="/api")
app.include_router(baby, prefix="/api")
app.include_router(rol, prefix="/api")
app.include_router(roles_user, prefix="/api")
