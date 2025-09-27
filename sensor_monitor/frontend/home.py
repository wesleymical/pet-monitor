import streamlit as st

st.title("Painel de Controle - Sensor Monitor")
st.write("Bem-vindo ao painel de controle!")

st.page_link("monitor.py", label="Ir para Monitor", icon="🔌")
st.page_link("simulator.py", label="Ir para Simulador", icon="🧪")