import streamlit as st
import requests
import pandas as pd

st.title("Relatório Analítico dos Sensores")

try:
    resp = requests.get("http://backend:8000/dados")
    dados = resp.json()["dados"]
    if dados:
        df = pd.DataFrame(dados)
        st.subheader("Resumo dos Dados")
        st.dataframe(df)

        st.subheader("Estatísticas")
        st.write("Temperatura")
        st.write(df["temperatura"].describe())

        st.write("Umidade")
        st.write(df["umidade"].describe())

        st.subheader("Gráficos")
        st.line_chart(df[["temperatura", "umidade"]])
    else:
        st.warning("Nenhum dado disponível para análise.")
except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")