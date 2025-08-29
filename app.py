import streamlit as st

st.title("😏 Oi gatinho...")
st.write("✨ Você aceita sair comigo?")

col1, col2 = st.columns(2)

if col1.button("Sim 😍"):
    st.success("Sabia que você ia dizer sim! Vamos ao Dalú 🍖")

if col2.button("Não 🥺"):
    st.error("Tudo bem... mas saiba que perdeu a chance de comer espetinho 🍢")
