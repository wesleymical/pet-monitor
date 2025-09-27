import streamlit as st
import pandas as pd
import json
import os

st.title("Painel de Sensores Domésticos")

DATA_PATH = "data/dados.json"

if os.path.exists(DATA_PATH):
    with open(DATA_PATH) as f:
        lines = f.readlines()
        data = [json.loads(line) for line in lines]

    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    st.line_chart(df.set_index("timestamp")[["temperatura", "umidade"]])
else:
    st.warning("Nenhum dado disponível ainda.")