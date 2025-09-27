import streamlit as st
import requests

st.title("Monitor de Sensores")

if st.button("Iniciar Monitor"):
    resp = requests.post("http://backend:8000/monitor/start")
    st.success(resp.json()["status"])

if st.button("Parar Monitor"):
    resp = requests.post("http://backend:8000/monitor/stop")
    st.warning(resp.json()["status"])