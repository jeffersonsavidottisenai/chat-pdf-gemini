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