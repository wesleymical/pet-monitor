import requests, random, time

URL = "http://localhost:8000/sensor"

while True:
    data = {
        "temperatura": round(random.uniform(20, 30), 2),
        "umidade": round(random.uniform(40, 60), 2)
    }
    try:
        response = requests.post(URL, json=data)
        print("Enviado:", data, "Resposta:", response.json())
    except Exception as e:
        print("Erro ao enviar:", e)
    time.sleep(5)