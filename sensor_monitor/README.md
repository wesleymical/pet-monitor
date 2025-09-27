
# Sensor Monitor

## Visão Geral

O Sensor Monitor é uma solução baseada em containers para monitoramento de sensores, simulação de dados e controle centralizado via painel web.
Utiliza FastAPI para o backend e Streamlit para o frontend, com navegação multipáginas.

---

## Estrutura do Projeto

```
sensor_monitor/
│   docker-compose.yml
│   iniciar_sensor_monitor.bat
│   parar_sensor_monitor.bat
│   README.md
│
├───backend
│       Dockerfile
│       main.py
│       requirements.txt
│       .dockerignore
│
├───data
│       dados.json
│
└───frontend
    │   Dockerfile
    │   home.py           # Página inicial do painel
    │   requirements.txt
    │   .dockerignore
    │
    └───pages
        │   1_Monitor.py      # Página de controle do monitor
        │   2_Simulator.py    # Página do simulador de dados
        │   3_Dashboard.py    # Página de visualização dos dados
```

---

## Tecnologias Utilizadas

- **FastAPI**Backend para APIs REST, recebimento e simulação de dados dos sensores.
- **Streamlit**Frontend web interativo, com navegação multipáginas para controle, simulação e visualização.
- **Docker & Docker Compose**
  Orquestração dos serviços em containers para fácil implantação e portabilidade.

---

## Como Executar

1. **Instale o Docker Desktop**[https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
2. **Abra o terminal na pasta do projeto**

   ```
   cd c:\Users\mical\Documents\pet-monitor\sensor_monitor
   ```
3. **Inicie todos os serviços**

   ```
   iniciar_sensor_monitor.bat
   ```

   ou

   ```
   docker compose up --build -d
   ```
4. **Acesse pelo navegador:**

   - Painel e páginas: [http://localhost:8501](http://localhost:8501)
   - API e Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Funcionalidades

- **Página Inicial:**Orientação para navegação pelo menu lateral.
- **Monitor:**Botões para iniciar e parar o monitor via API.
- **Simulador:**Botão para gerar dados simulados, com campo para quantidade.
- **Dashboard:**
  Visualização dos dados recebidos dos sensores.

---

## APIs Principais (FastAPI)

- `POST /sensor`Recebe dados do sensor.
- `POST /monitor/start`Inicia o monitor.
- `POST /monitor/stop`Para o monitor.
- `POST /simulator?qtd=N`Gera N dados simulados.
- `GET /dados`Retorna todos os dados recebidos.
- **Swagger:**
  Documentação automática disponível em `/docs`.

---

## Observações

- Os serviços se comunicam via API, facilitando o controle remoto.
- Os dados são salvos em `data/dados.json`.
- Para personalizar, edite os arquivos em `backend` e `frontend/pages`.

---

## Requisitos

- Docker Desktop (amd64 para Windows comum)
- Python 3.11 (para desenvolvimento local)

---

## Licença

Projeto para fins de prototipagem e estudo.
