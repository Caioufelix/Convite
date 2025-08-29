import streamlit as st
import time

# Configuração da página
st.set_page_config(
    page_title="Convite Especial 💖",
    page_icon="❤️",
    layout="centered"
)

# Personalizando cores com Markdown e CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f9e0ee;  /* fundo rosa clarinho */
    }
    .big-font {
        font-size:40px !important;
        color: #d6336c;
        text-align: center;
    }
    .medium-font {
        font-size:25px !important;
        color: #6f2dbd;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True
)

# Mensagens principais
st.markdown('<p class="big-font">😏 Oi gatinho...</p>', unsafe_allow_html=True)
st.markdown('<p class="medium-font">✨ Você aceita sair comigo?</p>', unsafe_allow_html=True)

# Botões centralizados
col1, col2, col3 = st.columns([1,2,1])

if col2.button("Sim 😍"):
    placeholder = st.empty()
    for i in range(3):
        placeholder.markdown(f"⏳ Carregando{'.' * (i+1)}")
        time.sleep(0.5)
    placeholder.success("Sabia que você ia dizer sim! Vamos ao Dalu 🍖", icon="🎉")

if col2.button("Não 🥺"):
    placeholder = st.empty()
    for i in range(3):
        placeholder.markdown(f"⏳ Carregando{'.' * (i+1)}")
        time.sleep(0.5)
    placeholder.error("Eu em, se fude lixo", icon="😢")

