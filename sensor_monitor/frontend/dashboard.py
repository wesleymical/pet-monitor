import streamlit as st
import requests

st.title("Dashboard de Sensores")

try:
    resp = requests.get("http://backend:8000/dados")
    dados = resp.json()["dados"]
    st.write("Dados dos sensores recebidos:")
    st.json(dados)
except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")