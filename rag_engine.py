from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import config
from models import AnaliseMamografia
import vector_store

class RAGService:
    def __init__(self):
        self.llm = ChatOllama(model=config.LLM_MODEL_NAME, temperature=0)
        self.retriever = vector_store.get_retriever()

    def _recuperar_contexto(self, query: str) -> str:
        docs = self.retriever.invoke(query)
        return "\n\n".join([doc.page_content for doc in docs])

    def extrair_dados_estruturados(self, query_foco: str = "Resumo do laudo") -> dict:
        """
        Extrai BI-RADS e Lateralidade forçando output JSON.
        """
        contexto = self._recuperar_contexto(query_foco)
        parser = JsonOutputParser(pydantic_object=AnaliseMamografia)

        prompt = PromptTemplate(
            template="""Você é um radiologista assistente.
            Analise o contexto abaixo extraído de um laudo de mamografia.
            
            CONTEXTO:
            {contexto}
            
            Extraia as informações seguindo estritamente este formato JSON:
            {format_instructions}
            """,
            input_variables=["contexto"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        chain = prompt | self.llm | parser
        return chain.invoke({"contexto": contexto})

    def perguntar_livre(self, pergunta: str) -> str:
        """
        Chat livre (Q&A) sobre o documento.
        """
        contexto = self._recuperar_contexto(pergunta)
        
        prompt = PromptTemplate.from_template(
            """Baseado APENAS no contexto médico abaixo, responda à pergunta.
            Se não souber, diga que a informação não consta no laudo.
            
            Contexto:
            {contexto}
            
            Pergunta: {pergunta}
            """
        )
        
        chain = prompt | self.llm
        response = chain.invoke({"contexto": contexto, "pergunta": pergunta})
        return response.content