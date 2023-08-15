from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv
import os
from views.FabricanteView import fabricante_router
from views.AcessorioView import acessorio_router
from views.ProcessadorView import processador_router
from views.MemoriaView import memoria_router
from views.ProprietarioView import proprietario_router
from views.CentroCustoView import centroCusto_router

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
app.include_router(processador_router)
app.include_router(memoria_router)
app.include_router(proprietario_router)
app.include_router(centroCusto_router)