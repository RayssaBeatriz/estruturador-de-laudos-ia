# 🎗️ Mammo RAG Local

Projeto de Processamento de Linguagem Natural (NLP) com **DeepSeek** e **LangChain** para extrair dados estruturados (BI-RADS e Lateralidade) de laudos de mamografia. O código foi modularizado para garantir total privacidade e execução local.

## 📂 Estrutura

* `main.py`: Script principal para execução (Menu CLI).
* `ingestion.py`: Leitura de PDFs, chunking e vetorização no banco de dados.
* `rag_engine.py`: Motor de RAG (Chat e Extração) conectado ao LLM local.
* `vector_store.py`: Gerenciamento do banco vetorial (ChromaDB) e embeddings.
* `models.py`: Definição dos schemas de dados (JSON/Pydantic).

## 🛠 Tecnologias

`Python` | `LangChain` | `Ollama (DeepSeek)` | `ChromaDB` | `HuggingFace`

## 🚀 Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/RayssaBeatriz/estruturador-de-laudos-ia
    cd estruturador-de-laudos-ia
    ```

2.  **Prepare o modelo local:**
    Certifique-se de ter o [Ollama](https://ollama.com) instalado e baixe o modelo:
    ```bash
    ollama pull deepseek-r1:7b
    ```

3.  **Instale as dependências:**
    ```bash
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    ```

4.  **Rode o projeto:**
    ```bash
    python main.py
    ```

## 📊 Modelo e Resultados

O sistema utiliza uma arquitetura **RAG (Retrieval-Augmented Generation)** rodando 100% localmente. Ele combina busca semântica (`sentence-transformers`) com a capacidade de raciocínio do **DeepSeek-R1** para estruturar informações médicas sem enviar dados sensíveis para a nuvem.
