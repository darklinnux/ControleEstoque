from fastapi import FastAPI

app = FastAPI()


@app.get("/v1")
def getUsuaruis():
    return {"Version": "0.0.1"}

###ROTAS USUÁRIOS###
@app.get("/v1/users")
def getUsuaruis():
    return {"Version": "0.0.1"}

###ROTAS NOTEBOOKS###
@app.get("/v1/notebooks")
def getUsuaruis():
    return {"Version": "0.0.1"}

