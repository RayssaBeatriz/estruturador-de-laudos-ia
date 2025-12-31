from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import vector_store
import config

def processar_pdf(caminho_arquivo_pdf: str):
    print(f"--- Iniciando ingestão de: {caminho_arquivo_pdf} ---")
    
    # 1. Carregar
    try:
        loader = PyPDFLoader(caminho_arquivo_pdf)
        docs = loader.load()
    except Exception as e:
        print(f"Erro ao ler PDF: {e}")
        return False

    # 2. Dividir (Split)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP
    )
    splits = text_splitter.split_documents(docs)
    print(f"Documento dividido em {len(splits)} chunks.")

    # 3. Vetorizar e Salvar
    vector_store.create_vectorstore(splits)
    
    print("--- Ingestão concluída com sucesso ---")
    return True