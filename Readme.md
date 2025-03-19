# create a pythyon virtual environment
pyenv virtualenv 3.12.5 deep_trace


## Install poetry

https://python-poetry.org/docs/#installing-with-the-official-installer
1- curl -sSL https://install.python-poetry.org | python3 -





# Teste Prático - Desenvolvedor Python (Inteligência Artificial)

## Objetivo
Criar um sistema baseado em multi-agentes para buscar e consolidar informações públicas sobre um cliente a partir do nome e telefone. O sistema deve utilizar frameworks modernos de IA para agentes autônomos (CrewAI, LangChain, LangGraph, entre outros) e realizar deep search para obter informações relevantes em fontes públicas como redes sociais e bancos de dados online.

## Cenário
Somos uma imobiliária digital especializada na venda de apartamentos novos na planta. Captamos leads através do site (https://myside.com.br), onde clientes interessados preenchem formulários com nome e telefone. Nosso time de SDRs entra em contato para qualificação, mas atualmente realizamos buscas manuais no Google, o que é ineficiente.
Queremos um sistema que automatize essa pesquisa e gere um perfil detalhado do cliente, incluindo:

- Nome completo
- Idade ou faixa etária
- Gênero
- Estado civil
- Localização aproximada
- Profissão / Empresa atual
- Presença em redes sociais (Instagram, Facebook, LinkedIn)
- Interesses (ex: esportes, viagens, tecnologia, etc.)
- Possíveis menções notícias ou artigos relevantes
- Verificação de processos ou ações (ex: )
- Imagens do cliente em redes sociais
- Análise de imagens para inferir informações adicionais (ex: estilo de vida ambientes frequentes, hobbies) Requisitos Técnicos (sugestões)
- Linguagem: Python
- Frameworks para agentes: CrewAI, LangChain, LangGraph ou similar
- Web Scraping / APIs: Selenium, BeautifulSoup, Scrapy, SerpAPI, etc.
- Orquestração: Celery, RabbitMQ ou similar
- Banco de dados: PostgreSQL, MongoDB ou SQLite (para armazenar perfis gerados)
- Análise de imagens: utilizar qualquer LLM capaz de realizar análise de imagens.
- Entrega: Aplicativo FastAPI com endpoint para consulta (ex: <span style="color:green">/buscar?nome=Fulano&telefone=999999999</span>)

## Tarefas do Teste

1.  Criar um sistema multiagentes que distribua as buscas entre diferentes fontes públicas.

3.  Implementar um agente que busque informações básicas do cliente:

<ul>
<ol type="a">
<li>nome completo</li>
    <li>CPF</li>
    <li>Empresa atual</li>
    <li>Participação societária</l>
</ol>
</ul>

3.  Implementar um agente que seja capaz de iniciar uma transação PIX, usando o telefone como chave, a partir do site de um banco. Isso pode ser extremamente útil para coletar dados do cliente como Nome Completo e CPF.
 
4.  Criar um agente que faça deep search (busca aprofundada) sobre o cliente procurando tudo que possa encontrar sobre ele na internet:

<ul>
    <ol type="a">
        <li>notícias</li>
        <li>artigos</li>
        <li>entrevistas</li>
        <li>redes sociais</li>
            <ol type="i">
                <li>linkedin</li>
                <li>instagram</li>
                <li>facebook</li>
            </ol>
        <li>menções relevantes</li>
    </ol>
</ul>

5.  Criar um agente que busque imagens e legendas do cliente nas redes sociais (considerar que o cliente tem perfil aberto):

<ul>
    <ol type="a">
        <li>linkedin</li>
        <li>instagram</li>
        <li>facebook</li>
    </ol>
</ul>

6.  Criar um agente que processe imagens (e legendas) do cliente, analisando possíveis informações inferidas nas fotos:

<ul>
    <ol type="a">
    <li>padrão de vida</li>
    <li>hobbies</li>
    <li>filhos</li>
    <li>interesses</li>
</ol>
</ul>


7.  Consolidar os dados coletados e gerar um resumo estruturado.
   
<ul>
    <ol type="a">
        <li>incluir no resultado todas as imagens relevantes encontradas.</li>
    </ol>
</ul>

8.  Expor um endpoint REST para consulta.

OBS: A implementação de todos os agentes acima não é obrigatória, porém desejável.

## Critérios de Avaliação

- **Correção técnica:** O sistema deve ser funcional e fornecer informações relevantes.
- **Uso adequado de multiagentes:** Agentes especializados devem trabalhar de forma distribuída.
- **Eficácia da deep search:** Capacidade de coletar informações relevantes e confiáveis.
- **Qualidade da análise de imagens:** Capacidade de identificar informações relevantes a partir das fotos.
- **Boas práticas de código:** Estrutura limpa, modular e bem documentada.
- **Desempenho:** Respostas rápidas e eficiente uso de recursos.

## Entrega

O candidato deve fornecer:
- Repositório Git com o código fonte e README explicando a solução.
- Instruções de instalação e execução.
- (Opcional) Demonstração em vídeo ou deploy online.
