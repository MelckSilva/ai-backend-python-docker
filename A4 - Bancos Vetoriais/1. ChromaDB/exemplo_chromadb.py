import chromadb
from sentence_transformers import SentenceTransformer

def main():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    
    client = chromadb.PersistentClient(path="./chroma_data")
    
    collection = client.get_or_create_collection(
        name="minha_colecao",
        metadata={"hnsw:space": "cosine"}
    )

    textos = [
        "A inteligência artificial está transformando a tecnologia.",
        "Bancos de dados vetoriais são essenciais para RAG.",
        "O aprendizado de máquina demanda muitos cálculos matemáticos.",
        "A receita de pão de queijo leva polvilho doce e azedo."
    ]
    ids = ["doc1", "doc2", "doc3", "doc4"]

    vetores = model.encode(textos).tolist()

    collection.upsert(
        ids=ids,
        documents=textos,
        embeddings=vetores
    )

    pergunta = "Como a Inteligência Artificial é usada em RAG?"
    vetor_pergunta = model.encode([pergunta]).tolist()
    
    resultados = collection.query(
        query_embeddings=vetor_pergunta,
        n_results=2
    )

    print(f"BUSCANDO POR: '{pergunta}'\n")
    for texto_encontrado in resultados["documents"][0]:
        print(f"-> {texto_encontrado}")

if __name__ == "__main__":
    main()
