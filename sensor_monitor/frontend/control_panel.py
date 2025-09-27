import streamlit as st
import requests
import random

st.title("Painel de Controle do Sensor Monitor")

st.header("Simulador de Dados")

qtd = st.number_input("Quantidade de dados para gerar", min_value=1, max_value=1000, value=1)
simular = st.button("Gerar Dados Simulados")

if simular:
    url = "http://backend:8000/sensor"  # Use 'backend' se rodando via docker-compose, 'localhost' se rodando local
    for i in range(qtd):
        data = {
            "temperatura": round(random.uniform(20, 30), 2),
            "umidade": round(random.uniform(40, 60), 2)
        }
        try:
            response = requests.post(url, json=data)
            st.success(f"Enviado {i+1}: {data} | Resposta: {response.json()}")
        except Exception as e:
            st.error(f"Erro ao enviar: {e}")

st.header("Monitoramento")
if st.button("Iniciar Monitor"):
    st.info("Monitor iniciado (implementar ação conforme necessidade).")

if st.button("Encerrar Monitor"):
    st.info("Monitor encerrado (implementar ação conforme necessidade).")