# LLMs, SLMs e Tool Calling - Principais Conceitos

Neste material, apresentamos os conceitos fundamentais sobre Modelos de Linguagem e como esses sistemas interagem com ferramentas de software externas.

## 1. LLMs (Large Language Models)
São modelos de linguagem de grande escala treinados em vastos conjuntos de dados e executados em clusters de alto desempenho.
- **Exemplos**: GPT-4, Claude 3, Gemini 3 Pro.
- **Uso ideal**: Indicados para tarefas que demandam alto nível de raciocínio lógico, geração de código complexo ou compreensão de instruções detalhadas e com diversas nuances.
- **Custo**: Operam predominantemente na nuvem, com modelo de cobrança baseado na quantidade de tokens processados via API.

## 2. SLMs (Small Language Models)
São versões condensadas e otimizadas dos modelos de linguagem, projetadas para operar com menor consumo de recursos.
- **Exemplos**: Llama 3 (8B), Phi-3, Mistral, Gemma.
- **Uso ideal**: Adequados para execução local (inferência na própria máquina ou em servidores corporativos isolados), oferecendo baixa latência em tarefas mais estruturadas e diretas.
- **Vantagem Principal**: Garantem a privacidade total dos dados, uma vez que as informações não necessitam ser enviadas para infraestruturas em nuvem de terceiros.

## 3. Tool Calling (Function Calling)
Consiste na capacidade de um modelo de inteligência artificial de não apenas gerar respostas em linguagem natural, mas também retornar solicitações estruturadas para a execução de funções sistêmicas.

### Fluxo de Execução:
1. O texto do usuário (Prompt) é enviado ao modelo.
2. Juntamente com o Prompt, fornece-se o mapeamento das ferramentas disponíveis na aplicação (nome da função, descrição e parâmetros mapeados).
3. Ao avaliar a necessidade de uma informação externa (por exemplo, "Qual a previsão do tempo?"), a Inteligência Artificial retorna um objeto estruturado (tipicamente em JSON) indicando a necessidade de invocar a ferramenta correspondente, como `get_weather(cidade="Bauru")`.
4. O código Python intercepta essa solicitação e executa a lógica apropriada.
5. O resultado processado é retornado à IA.
6. A Inteligência Artificial consolida a informação recebida e elabora a resposta final em linguagem natural.

### Competências essenciais desenvolvidas com esta abordagem:
- Extração de intenções a partir de comandos em linguagem natural.
- Seleção condicional de funções baseada no contexto semântico.
- Mapeamento adequado dos argumentos textuais para tipos de dados sistêmicos (Strings, Floats, Booleanos).
- Estruturação de agentes autônomos orientados por rotinas dinâmicas.
