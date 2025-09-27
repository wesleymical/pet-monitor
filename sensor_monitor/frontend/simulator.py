import streamlit as st
import requests

st.title("Simulador de Dados")

qtd = st.number_input("Quantidade de registros", min_value=1, max_value=1000, value=1)
if st.button("Gerar Dados"):
    resp = requests.post("http://backend:8000/simulator", params={"qtd": qtd})
    st.success(f'{resp.json()["total"]} registros simulados!')