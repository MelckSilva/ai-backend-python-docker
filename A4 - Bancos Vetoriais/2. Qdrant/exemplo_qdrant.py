import qdrant_client
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer

def main():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    vector_size = model.get_embedding_dimension()
    
    client = qdrant_client.QdrantClient(host="localhost", port=6333)
    
    if not client.collection_exists("minha_colecao_qdrant"):
        client.create_collection(
            collection_name="minha_colecao_qdrant",
            vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
        )

    textos = [
        "A inteligência artificial está transformando a tecnologia.",
        "Bancos de dados vetoriais são essenciais para RAG.",
        "O aprendizado de máquina demanda muitos cálculos matemáticos.",
        "A receita de pão de queijo leva polvilho doce e azedo."
    ]
    
    vetores = model.encode(textos).tolist()

    pontos = [
        PointStruct(id=indice+1, vector=vetores[indice], payload={"texto": textos[indice]})
        for indice in range(len(textos))
    ]
    client.upsert(collection_name="minha_colecao_qdrant", points=pontos)

    pergunta = "Como a Inteligência Artificial é usada em RAG?"
    vetor_pergunta = model.encode([pergunta])[0].tolist()
    
    resultados = client.query_points(
        collection_name="minha_colecao_qdrant",
        query=vetor_pergunta,
        limit=2
    ).points

    print(f"BUSCANDO POR: '{pergunta}'\n")
    for resultado in resultados:
        print(f"-> {resultado.payload['texto']}")

if __name__ == "__main__":
    main()
