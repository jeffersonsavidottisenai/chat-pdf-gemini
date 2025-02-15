# Chat com PDF usando a API do Gemini

## 1️⃣ Preparando o Ambiente

### Criar e ativar o ambiente virtual
```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### Criar o arquivo de dependências (`requirements.txt`)
```txt
google-generativeai
pypdf
streamlit
python-dotenv
```

### Instalar as dependências
```bash
pip install -r requirements.txt
```

---

## 2️⃣ Extração de Texto do PDF (`src/extract.py`)
```python
import pypdf  # Biblioteca para manipulação de PDFs

def extract_text_from_pdf(pdf_file):
    """
    Função para extrair o texto de um PDF carregado no Streamlit.
    
    Parâmetros:
    pdf_file (UploadedFile): Arquivo PDF carregado pelo usuário.

    Retorna:
    str: Texto extraído do PDF.
    """
    reader = pypdf.PdfReader(pdf_file)  # Cria um objeto para ler o PDF
    
    # Percorre todas as páginas e extrai o texto disponível
    text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text  # Retorna o texto extraído
```

---

## 3️⃣ Criando a Conexão com a API do Gemini (`src/gemini_api.py`)
```python
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
```

---

## 4️⃣ Criando a Interface do Chat com Streamlit (`src/main.py`)
```python
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
```

---

## 5️⃣ Estrutura do Projeto no Visual Studio Code
```
📂 chat-pdf-gemini
│── 📂 venv                # Ambiente virtual
│── 📂 data                # Pasta para armazenar PDFs (opcional)
│── 📂 src                 # Código-fonte
│   │── 📜 __init__.py     # Torna `src` um módulo Python (adicione este arquivo)
│   │── 📜 main.py         # Arquivo principal (Streamlit)
│   │── 📜 extract.py      # Extração de texto do PDF
│   │── 📜 gemini_api.py   # Comunicação com a API do Gemini
│── 📜 .env                # Armazena a chave da API do Gemini
│── 📂 assets              # Imagens/arquivos auxiliares (opcional)
│── 📜 .gitignore          # Arquivo para ignorar arquivos desnecessários
│── 📜 README.md           # Documentação do projeto
```

---

## 6️⃣ Como Rodar o Projeto
```bash
# Ativar o ambiente virtual
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Criar arquivo .env e adicionar a chave da API
# No arquivo .env:
GEMINI_API_KEY=SUACHAVEAQUI

# Rodar o Streamlit
streamlit run src/main.py
```
