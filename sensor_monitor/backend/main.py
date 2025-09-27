from fastapi import FastAPI, Request
import json
from datetime import datetime
import os
import subprocess
import random

app = FastAPI()

DATA_PATH = "data/dados.json"
os.makedirs("data", exist_ok=True)

@app.post("/sensor")
async def receive_data(request: Request):
    data = await request.json()
    data["timestamp"] = datetime.now().isoformat()
    with open(DATA_PATH, "a") as f:
        f.write(json.dumps(data) + "\n")
    return {"status": "ok", "data": data}

@app.post("/monitor/start")
def start_monitor():
    # Exemplo: iniciar serviço (substitua pelo comando real)
    # subprocess.Popen(["docker", "compose", "up", "-d"])
    return {"status": "Monitor iniciado"}

@app.post("/monitor/stop")
def stop_monitor():
    # Exemplo: parar serviço (substitua pelo comando real)
    # subprocess.Popen(["docker", "compose", "down"])
    return {"status": "Monitor parado"}

@app.post("/simulator")
def simulate_data(qtd: int = 1):
    for i in range(qtd):
        data = {
            "temperatura": round(random.uniform(20, 30), 2),
            "umidade": round(random.uniform(40, 60), 2),
            "timestamp": datetime.now().isoformat()
        }
        with open(DATA_PATH, "a") as f:
            f.write(json.dumps(data) + "\n")
    return {"status": "ok", "total": qtd}

@app.get("/dados")
def get_dados():
    try:
        with open(DATA_PATH, "r") as f:
            linhas = f.readlines()
            dados = [json.loads(linha) for linha in linhas if linha.strip()]
        return {"dados": dados}
    except Exception as e:
        return {"erro": str(e), "dados": []}