from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv
import os
from views.FabricanteView import fabricante_router
from views.AcessorioView import acessorio_router

load_dotenv()

app = FastAPI()
router = APIRouter()

#print(os.getenv('DATABASE_URL'))
@app.get("/")
def getUsuaruis():
    return {"Version": "0.0.1"}

###ROTAS FABRICANTE###
app.include_router(fabricante_router)
app.include_router(acessorio_router)