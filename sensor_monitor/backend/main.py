from fastapi import FastAPI, Request
import json
from datetime import datetime
import os

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