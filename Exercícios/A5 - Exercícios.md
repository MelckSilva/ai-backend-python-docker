# Exercício Prático: Chatbot com Memória + RAG

## Contexto
Desenvolver um chatbot para uma clínica médica, capaz de responder dúvidas de pacientes utilizando contexto real.

---

## Objetivo
Criar um bot que utilize:
- Memória de conversa (session_id)
- Banco vetorial (RAG)
- LLM (ex: Groq)

---

## Requisitos

### 1. Chat básico
- Entrada via terminal
- user_id e session_id
- Comando `/new` para nova sessão

---

### 2. Memória (curto prazo)
- Armazenar últimas mensagens (window)
- Limite de aproximadamente 10 interações

---

### 3. Banco Vetorial (obrigatório)
Utilizar:
- ChromaDB ou
- Qdrant

---

### 4. Base de Conhecimento
Criar entre 10 e 20 textos, por exemplo:
- Horários de atendimento
- Convênios aceitos
- Tipos de exames
- Regras da clínica

---

### 5. RAG (obrigatório)
Fluxo:
1. Receber pergunta do usuário
2. Buscar contexto no banco vetorial
3. Injetar contexto no prompt
