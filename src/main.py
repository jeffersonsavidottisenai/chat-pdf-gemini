import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.extract import extract_text_from_pdf
from src.gemini_api import ask_gemini

# Título da aplicação
st.title("Chat com PDF usando Gemini")

# Upload do arquivo PDF
uploaded_file = st.file_uploader("Faça upload de um PDF", type=["pdf"])

# Se um arquivo for carregado, extrai o texto e armazena na sessão
if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    st.session_state["context"] = text

# Campo de entrada para a pergunta do usuário
question = st.text_input("Digite sua pergunta:")

# Se houver uma pergunta e um contexto carregado, chama a API do Gemini
if question and "context" in st.session_state:
    response = ask_gemini(question, st.session_state["context"])
    st.write("### Resposta:")
    st.write(response)  # Exibe a resposta gerada pelo Gemini