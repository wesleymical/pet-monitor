FROM python:3.11-slim
WORKDIR /app

# Copie apenas o requirements.txt e instale as dependências primeiro
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Depois copie o restante do código
COPY . .

CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]