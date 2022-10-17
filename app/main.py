from fastapi import FastAPI
from . import models
from .database import engine
from .routers import users, posts, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)
# fetch('http://localhost:8000/').then(res=>res.json()).then(console.log)

app = FastAPI()

# origins = ["https://www.google.com", "https://www.youtube.com"]
origins = ["*"]         # esto hace que la api este abierto para todos lo que sirve para testearla pero no es lo mejor en temas de seguridad

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Welcome to my API!!!!!!!"}