# Retrieval-Augmented Generation (RAG) - Principais Conceitos

Este material introduz os blocos de construção de um fluxo de dados RAG, uma técnica largamente adotada para permitir que Modelos de Linguagem consultem bases de conhecimento restritas ou proprietárias de forma eficiente.

## 1. O que é RAG?
A técnica de **Retrieval-Augmented Generation** (Geração Aumentada por Recuperação) propõe não depender exclusivamente dos parâmetros e conhecimentos pré-treinados do modelo. Em vez de exigir que a IA detenha a informação de antemão, o sistema busca ativamente os dados relevantes na base local (Retrieval) e os fornece no Prompt, orientando a IA a gerar a resposta baseando-se apenas neste contexto fornecido (Generation).

## 2. Ingestão de Dados (Preparação)

#### Passo 1: Extração (Parsing)
A etapa inicial consiste na extração do texto bruto de documentos complexos, tais como PDFs, planilhas ou sistemas web, convertendo toda a base informacional em cadeias de texto estruturadas por intermédio do Python (ex: uso do PyMuPDF, pdfplumber).

#### Passo 2: Fatiamento (Chunking)
Dado que documentos extensos não podem ser inseridos de forma integral no contexto do modelo devido à limitação de tokens, promove-se a fragmentação textual (Chunking):
- Preserva o limite de memória contextual aceito pelo modelo empregado.
- Impede que múltiplos assuntos não relacionados se fundam numa só busca.
- Reduz os custos operacionais (quantidade de tokens enviados à API a cada transação).

## 3. Busca e Rastreamento (Retrieval)

#### Passo 3: Geração de Embeddings
Através da utilização de modelos de representação vetorial (Sentence Transformers), o sistema converte os segmentos de texto (Chunks) em extensos arrays numéricos, denominados vetores. Conceitos literários que compartilham similaridade semântica tendem a convergir, gerando coordenadas matemáticas muito próximas.

#### Passo 4: Armazenamento em Banco de Dados
Para contornar o retrabalho computacional, todos os vetores recém-criados são atrelados num repositório focado na estrutura matemática - os Bancos de Dados Vetoriais. Estas plataformas arquivam o vetor concomitantemente ao texto de origem.

#### Passo 5: Recuperação de Conhecimento
No momento em que o usuário formula sua pergunta, converte-se este texto originário nas mesmas dimensões vetoriais dos documentos. Em seguida, busca-se no banco de dados quais são os locais das distâncias mais estreitas e, portanto, de resposta mais oportuna ao tema perguntado.

## 4. Geração Final (Generation)

#### Passo 6: Injeção no Prompt
Nesta etapa, reúnem-se as partes obtidas no banco dentro da premissa fundamental a ser processada pelo modelo de Inteligência Artificial:
```text
"Você é o assistente técnico. Utilizando EXCLUSIVAMENTE o contexto listado abaixo, responda à questão formalizada pelo usuário.

CONTEXTO OBTIDO DA BASE DE DADOS: {chunks_resgatados}

PERGUNTA DO USUÁRIO: {pergunta_direta_usuario}"
```

#### Passo 7: Resposta Sintetizada
Diante dessas restrições, o LLM restringe sua capacidade generativa ao texto de referência, combinando seus predicados linguísticos inatos com as políticas locais encontradas, promovendo um resultado gramaticalmente acessível e estritamente correto no escopo do negócio.
