import os

# Caminhos
DB_PATH = "./chroma_db_mamografias"
PDF_DIR = "./documentos_pdf"

# Modelos
LLM_MODEL_NAME = "phi3" 

# Modelo de Embedding 
EMBEDDING_MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

# Parâmetros de Chunking
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200