# Exercícios - Retrieval-Augmented Generation (RAG) em Python 

Estes exercícios têm como objetivo ensinar na prática o conceito de RAG (Retrieval-Augmented Generation), construindo passo a passo a habilidade de extrair textos, dividi-los, convertê-los em embeddings, buscar os trechos mais relevantes e usá-los como contexto para uma IA responder perguntas.

Os exercícios começam com a manipulação básica de texto e evoluem até a construção de um pipeline RAG completo usando LLMs.

---

# Exercício 1 - Extração de Texto de um Documento

Baixe ou crie um arquivo PDF ou TXT (exemplo: `historia.txt` ou `artigo.pdf`). O objetivo deste exercício é puramente ler o conteúdo deste documento e exibi-lo no console.

Para TXT, use leitura nativa do Python.
Para PDF, instale e use uma biblioteca como `PyMuPDF` (`fitz`) ou `pdfplumber`.

**Resultado Esperado:** O script deve imprimir o texto inteiro do documento criado.

---

# Exercício 2 - Estratégia de Chunking (Divisão de Texto)

LLMs possuem limite de tokens e bancos vetoriais funcionam melhor com pequenos blocos de texto.

**O que fazer:**
Crie uma função `dividir_texto(texto, tamanho_chunk)` que receba um texto grande (do Exercício 1) e o divida em blocos que não ultrapassem o limite de caracteres estipulado.

```python
def dividir_texto(texto, tamanho_chunk=500):
    # Sua lógica para dividir o texto aqui
    pass
```

**Resultado Esperado:** Imprima a quantidade de "chunks" (blocos) que foram gerados e o conteúdo do primeiro e do último chunk para verificar.

---

# Exercício 3 - Gerando Embeddings Locais

Vamos usar a biblioteca `sentence-transformers` para transformar os textos em vetores matemáticos, que são compreendidos pela máquina para calcular semelhança.

1. Instale o pacote: `pip install sentence-transformers`.
2. Carregue o modelo `all-MiniLM-L6-v2`.
3. Passe três frases distintas e imprima o vetor resultante da primeira frase (você notará que é uma grande lista de números decimais).

---

# Exercício 4 - Criando um Banco de Conhecimento em Memória (Sem Chroma/Qdrant)

Antes de usar Bancos Vetoriais complexos, vamos simular uma busca semântica puramente no Python para entender a matemática.

**O que fazer:**
1. Crie uma lista com 5 fatos aleatórios, como:
   - "O pão de queijo é originário de Minas Gerais."
   - "A Terra gira em torno do Sol."
   - "A capital da França é Paris."
2. Transforme todos os fatos em vetores (Embeddings) usando o Exercício 3.
3. Peça ao usuário para digitar uma pergunta.
4. Transforme a pergunta em vetor.
5. Calcule a distância (usando bibliotecas como `scipy.spatial.distance.cosine` ou `np.dot` se usar numpy) entre o vetor da pergunta e os vetores dos fatos.

**Resultado Esperado:** O programa deve imprimir o fato da lista que mais se assemelha à pergunta digitada.

---

# Exercício 5 - O "R" e o "G" do RAG (Retrieval + Generation)

Agora vamos juntar a busca do Exercício 4 (Retrieval) com um LLM para a Geração de Texto (Generation).

**O que fazer:**
1. Reaproveite o código de busca do fato mais semelhante (Exercício 4).
2. Conecte-se a uma API de LLM (como OpenAI, Gemini, ou Ollama local).
3. Em vez de apenas imprimir o fato mais semelhante, injete esse fato no "System Prompt" do LLM.

Exemplo de Prompt a ser gerado dinamicamente:
```
Você é um assistente prestativo.
Responda à pergunta do usuário baseando-se EXCLUSIVAMENTE neste contexto:
CONTEXTO: {fato_mais_relevante_encontrado_no_exercicio_4}
```

4. Envie a pergunta do usuário para o LLM e mostre a resposta caprichada que ele vai gerar baseada no contexto.

---

# Exercício 6 - Pipeline RAG Completo (Desafio Final)

Chegou a hora de juntar tudo em um código profissional. Crie um script final que execute a seguinte jornada do início ao fim:

1. **Ingestão:** Leia um arquivo `.txt` longo simulando um regulamento de empresa ou base de dados (Ex: `regras_empresa.txt`).
2. **Chunking:** Divida-o em blocos de 500 caracteres.
3. **Indexação:** Transforme-os em Embeddings e armazene em bancos vetoriais.
4. **Busca (Retrieval):** O usuário faz uma pergunta no terminal. Você localiza o chunk (ou os 2 chunks) mais relevantes.
5. **Geração (Generation):** Adicione os chunks encontrados num Prompt estruturado e envie para a API de um LLM responder.

**Exemplo de uso:**
*Usuário:* "Quantos dias de férias posso tirar?"
*Sistema:* Faz a busca, acha a regra (que era gigante e estava na página 4 do TXT), insere no LLM e retorna: "De acordo com as regras da empresa, você tem direito a 30 dias após um ano de contribuição."


