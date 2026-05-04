"""
    ATENÇÃO – CÓDIGO EDUCACIONAL (NÃO UTILIZAR EM PRODUÇÃO)

    Este código foi desenvolvido exclusivamente para fins didáticos,
    no contexto da disciplina Tecnologias e Programação Integrada.

    O objetivo é demonstrar a instrumentação e observabilidade em 
    aplicações LLM (LLMOps) utilizando o Langfuse.

    IMPORTANTE:
    - Este código NÃO possui guardrails de segurança.
    - Não há validação robusta de entrada.
    - Não há controle de permissões ou autenticação.
    - Não há proteção contra uso indevido, chamadas indevidas ou escrita não autorizada.
    - NÃO deve ser executado em ambientes de produção.

    Autor: Prof. Victor

"""
import os
import uuid
from dotenv import load_dotenv
from groq import Groq
from langfuse.decorators import observe, langfuse_context

load_dotenv()

client = Groq()


@observe(as_type="generation")
def gerar_resposta(mensagem_usuario: str, model: str = "openai/gpt-oss-120b"):
    langfuse_context.update_current_observation(
        name="Geracao_Groq",
        model=model,
        input=mensagem_usuario,
        metadata={"user_input_length": len(mensagem_usuario)}
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "Você é um assistente acadêmico útil, especializado em IA."},
            {"role": "user", "content": mensagem_usuario}
        ],
        temperature=0.7,
        max_tokens=200
    )

    texto_resposta = response.choices[0].message.content
    langfuse_context.update_current_observation(output=texto_resposta)
    return texto_resposta


@observe()
def exemplo1():
    print("\nEXEMPLO 1 — Chamada com rastreamento (Tracing) no Langfuse\n")
    session_id = str(uuid.uuid4())
    langfuse_context.update_current_trace(
        name="Exemplo1_Trace_Simples",
        session_id=session_id,
        user_id="aluno_123"
    )

    pergunta = input("Pergunta: ")
    resposta = gerar_resposta(pergunta)
    print("\nResposta:\n", resposta)
    print("\n[INFO] Trace enviado para o Langfuse.")


def main():
    while True:
        print("\n==============================")
        print("AULA OBSERVABILIDADE - Exemplos")
        print("==============================")
        print("1 - Chamada Simples (Trace)")
        print("0 - Sair")

        op = input("\nEscolha: ")

        if op == "1":
            exemplo1()

        elif op == "0":
            print("\nEncerrando e enviando logs restantes para o Langfuse...")
            langfuse_context.flush()
            break

if __name__ == "__main__":
    main()
