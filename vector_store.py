from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import config

def get_embedding_function():
    """Retorna a função de embedding configurada."""
    return HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL_NAME)

def get_vectorstore():
    """Carrega o banco vetorial existente."""
    return Chroma(
        persist_directory=config.DB_PATH,
        embedding_function=get_embedding_function()
    )

def create_vectorstore(documents):
    """Cria ou atualiza o banco com novos documentos."""
    return Chroma.from_documents(
        documents=documents,
        embedding=get_embedding_function(),
        persist_directory=config.DB_PATH
    )

def get_retriever(k=3):
    """Retorna o objeto retriever configurado."""
    vectorstore = get_vectorstore()
    return vectorstore.as_retriever(search_kwargs={"k": k})