from fastapi import FastAPI
from routes.personas import person
from routes.users import user
from routes.nacimientos import baby
from routes.roles import rol
from routes.roles_user import roles_user
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]
# configuracion del middleware para la insersion en la base
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# añadimos las rutas de nuestras tablas a nuestra api
app.include_router(person, prefix="/api")
app.include_router(user, prefix="/api")
app.include_router(baby, prefix="/api")
app.include_router(rol, prefix="/api")
app.include_router(roles_user, prefix="/api")
