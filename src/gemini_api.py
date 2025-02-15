import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Verifica se a chave foi carregada corretamente
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Erro: A variável GEMINI_API_KEY não foi encontrada. Verifique o arquivo .env.")

# Configuração da API do Gemini
genai.configure(api_key=api_key)


def ask_gemini(question, context):
    """
    Função que envia uma pergunta para a API do Gemini com base no texto do PDF.

    Parâmetros:
    question (str): Pergunta feita pelo usuário.
    context (str): Texto extraído do PDF que será usado para responder.

    Retorna:
    str: Resposta gerada pelo modelo da Gemini.
    """
    model = genai.GenerativeModel("gemini-pro")  # Inicializa o modelo Gemini
    
    # Gera a resposta com base no contexto do PDF e na pergunta fornecida
    response = model.generate_content(f"Baseado neste documento:\n\n{context}\n\nResponda: {question}")
    return response.text  # Retorna a resposta gerada pelo Gemini