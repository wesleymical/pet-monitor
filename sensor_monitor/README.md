
# Sensor Monitor

## Visão Geral

O Sensor Monitor é uma solução para monitoramento de sensores, simulação de dados e controle centralizado via painel web.
A arquitetura utiliza containers Docker, API com FastAPI e interface web com Streamlit.

---

## Estrutura do Projeto

```
sensor_monitor/
│   docker-compose.yml
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
├───frontend
│       Dockerfile
│       requirements.txt
│       .dockerignore
│       home.py           # Painel de controle (página inicial)
│       monitor.py        # Página do monitor (controle via API)
│       simulator.py      # Página do simulador (controle via API)
│       dashboard.py      # Página de visualização dos dados
```

---

## Frameworks e Tecnologias

- **FastAPI**Framework moderno e rápido para construção de APIs REST em Python.Utilizado no backend para receber dados dos sensores, controlar o monitor e simular dados.
- **Streamlit**Framework para criação rápida de interfaces web interativas em Python.Utilizado no frontend para o painel de controle, monitor, simulador e dashboard.
- **Docker & Docker Compose**
  Orquestração dos serviços em containers, garantindo portabilidade e facilidade de implantação.

---

## Como Executar

1. **Instale o Docker Desktop**[https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
2. **Abra o terminal na pasta do projeto**

   ```
   cd c:\Users\mical\Documents\pet-monitor\sensor_monitor
   ```
3. **Inicie todos os serviços**

   ```
   docker compose up --build -d
   ```
4. **Acesse os sistemas:**

   - **Backend (API e Swagger):** [http://localhost:8000/docs](http://localhost:8000/docs)
   - **Dashboard:** [http://localhost:8501](http://localhost:8501)
   - **Painel de Controle:** [http://localhost:8501] (página inicial do Streamlit)
   - **Monitor:** [http://localhost:8501/monitor]
   - **Simulador:** [http://localhost:8501/simulator]

---

## Funcionalidades

- **Painel de Controle (home):**

  - Navegação para monitor, simulador e dashboard
- **Monitor:**

  - Botões para iniciar e parar o monitor via API
- **Simulador:**

  - Botão para gerar dados simulados, com campo para quantidade
- **Dashboard:**

  - Visualização dos dados recebidos dos sensores

---

## APIs Principais (FastAPI)

- `POST /sensor`Recebe dados do sensor
- `POST /monitor/start`Inicia o monitor
- `POST /monitor/stop`Para o monitor
- `POST /simulator?qtd=N`Gera N dados simulados
- **Swagger:**
  Documentação automática disponível em `/docs`

---

## Observações

- Os serviços se comunicam via API, facilitando o controle remoto.
- Os dados são salvos em `data/dados.json`.
- Para personalizar, edite os arquivos em `backend` e `frontend`.

---

## Requisitos

- Docker Desktop (amd64 para Windows comum)
- Python 3.11 (para desenvolvimento local)

---

## Licença

Projeto para fins de prototipagem e estudo.
