
# Sensor Monitor

## Estrutura

- **backend/**: API FastAPI para receber dados dos sensores.
- **frontend/**: Dashboard Streamlit para visualização dos dados.
- **data/**: Armazenamento dos dados recebidos.
- **docker-compose.yml**: Orquestração dos serviços.

## Como rodar

1. Instale o [Docker Desktop](https://www.docker.com/products/docker-desktop/) (amd64 para Windows comum).
2. No terminal, navegue até a pasta `sensor_monitor`.
3. Execute:
   ```
   docker compose up --build
   ```
4. Acesse:
   - Backend: [http://localhost:8000](http://localhost:8000)
   - Frontend: [http://localhost:8501](http://localhost:8501)

## API

- **POST /sensor**
  Recebe dados do sensor em JSON.

## Swagger

Acesse a documentação automática do FastAPI em:
[http://localhost:8000/docs](http://localhost:8000/docs)
