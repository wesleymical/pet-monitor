FROM python:3.11-slim
WORKDIR /app

# Atualize os pacotes do sistema para reduzir vulnerabilidades
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Copie apenas o requirements.txt e instale as dependências primeiro
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Depois copie o restante do código
COPY . .

CMD ["streamlit", "run", "home.py", "--server.port=8501", "--server.address=0.0.0.0"]