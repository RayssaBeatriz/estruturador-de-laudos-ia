import sys
import ingestion
from rag_engine import RAGService

def main():
    print("=== Sistema RAG Mamografia (DeepSeek Local) ===")
    
    # Menu simples para teste
    while True:
        print("\n1. Ingerir novo PDF")
        print("2. Extrair BI-RADS e Lateralidade")
        print("3. Fazer pergunta ao Chat")
        print("q. Sair")
        
        opcao = input("Escolha: ")

        if opcao == "1":
            path = input("Caminho do PDF: ")
            path = path.strip('"').strip("'")
            ingestion.processar_pdf(path)
            
        elif opcao == "2":
            try:
                service = RAGService()
                print("Analisando documentos vetoriais...")
                # Passamos uma query genérica para buscar o contexto geral do laudo
                resultado = service.extrair_dados_estruturados("Conclusão e achados do laudo")
                print("\n--- Resultado Estruturado ---")
                print(f"BI-RADS: {resultado.get('bi_rads')}")
                print(f"Lateralidade: {resultado.get('lateralidade')}")
                print(f"Resumo: {resultado.get('resumo_achados')}")
            except Exception as e:
                print(f"Erro: {e} (Você já ingeriu algum PDF?)")

        elif opcao == "3":
            pergunta = input("Sua pergunta: ")
            service = RAGService()
            resposta = service.perguntar_livre(pergunta)
            print(f"\nRespposta: {resposta}")
            
        elif opcao.lower() == "q":
            break

if __name__ == "__main__":
    main()