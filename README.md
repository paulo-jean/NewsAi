# Sua Newsletter Pessoal Automatizada com IA! 📰🤖

Este projeto Python gera uma newsletter personalizada com notícias sobre Inteligência Artificial e o Corinthians (ou sobre os temas que o usuário quiser), extraídas da web e resumidas usando LLMs (Large Language Models). Ele automatiza todo o processo, desde a coleta das notícias até o envio do email. 💌


## Como Funciona

O script possuí dois modos de coleta de informações, na versão 1 usa técnica de web scraping para extrair notícias de sites predefinidos que o usuário gosta de ler e acompanhar. Em seguida, utiliza LLMs (atualmente, Gemini e um modelo Groq) para resumir as notícias e formatá-las como uma newsletter em HTML. Por fim, envia a newsletter por email usando o Outlook (podendo ser configurado para usar com o gmail, alterando a biblioteca e fazendo outros ajustes na parte do envio de email).
Na versão 2, invés do web scraping, utiliza-se a API do DuckDuckGo (um motor de buscas na internet) para pesquisar por notícias recentes sobre o assunto predefinido e depois passar para os LLMs.

⚠️ Obs* Use o script da versão 1 com moderação e lembre-se que fazer scraping de sites que não autorizam a divulgação dos conteúdos ou comercialização dos mesmos pode gerar processos judiciais para quem o pratica. No meu caso, é para uso pessoal, por isso chamo o scrip de Newsletter Pessoal. É como se eu estivesse indo todo dia como de costume ao site e consumir as notícias daquele dia, porém de forma automatizada. Por fim, sempre leia os termos de cada site para saber o que pode ou não ser feito 😉

**Passo a passo:**

1. **Coleta de Notícias:** Extrai notícias sobre os temas dos sites escolhidos utilizando técnicas de web scraping, incluindo título, imagem e link.
2. **Resumo com LLMs:** Processa as notícias extraídas com LLMs para gerar um resumo conciso e informativo. Duas funções principais, `cnn_newsletter()` e `corinthians_newsletter()`, utilizam prompts específicos para orientar os LLMs na criação do resumo.
3. **Conversão para HTML:** Formata a newsletter em HTML usando um LLM para gerar o código HTML a partir do texto do resumo. A função `converter_html()` garante que a newsletter seja formatada corretamente para exibição em clientes de email.
4. **Envio de Email:** Envia a newsletter formatada em HTML por email usando a biblioteca `win32com` para interagir com o Outlook.


## Tecnologias e Bibliotecas Utilizadas

* **Python:** A linguagem de programação principal.
* **Beautiful Soup:** Para web scraping (extração de conteúdo da web).
* **Requests:** Para fazer requisições HTTP.
* **LangChain:** Um framework para desenvolvimento de aplicações com LLMs.
* **Groq:** Plataforma de LLM.
* **Google Generative AI:**  Plataforma de LLM (Gemini).
* **DuckDuckGo Search API:**  Para pesquisa na web.
* **win32com:** Para interagir com o Outlook.
* **datetime:** Para obter a data atual.

## Como Executar

1. **Pré-requisitos:**
    * Python 3 instalado.
    * Instale as bibliotecas: `pip install beautifulsoup4 requests langchain langchain-groq langchain-google-genai duckduckgo-search pywin32`
    * Configure as suas credenciais de API para o Groq, Google Generative AI e o Outlook.
2. **Configure as Chaves de API:** Substitua `'MY_KEY'`  pelas suas chaves de API do Groq e Google Generative AI.
3. **Configure os Cabeçalhos:** Substitua `MY_HEADERS` pelos cabeçalhos HTTP necessários, como User-Agent.
4. **Execute o Script:** `python seu_script.py`

## Possíveis Melhorias

* **Modularização:** Separar as diferentes partes do código em funções ou classes menores para melhor organização e reutilização.
* **Tratamento de Erros:** Adicionar tratamento de erros mais robusto, como tentar novamente em caso de falha na requisição web ou no LLM.
* **Agendamento:** Implementar agendamento diretamente por código para que a newsletter seja gerada e enviada automaticamente em intervalos regulares.
* **Testes:** Adicionar testes unitários para garantir a qualidade do código.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.
