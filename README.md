## API de Busca de Vagas de Emprego
Esta é uma aplicação FastAPI que permite buscar vagas de emprego em Maringá, Brasil, com base em palavras-chave específicas. A aplicação possui uma interface HTML simples para inserir os critérios de busca e exibe os resultados em JSON.

## Requisitos
Python 3.6 ou superior
FastAPI
BeautifulSoup (para análise HTML)
Pydantic (para validação de dados)
Instalação do Miniconda

## Instalação
Clone este repositório em seu sistema local:

bash
Copy code:
git clone https://github.com/seu-usuario/nome-do-repositorio.git
Navegue até o diretório do projeto:

bash
Copy code:
cd nome-do-repositorio
Crie e ative um ambiente virtual (opcional, mas recomendado):

bash
Copy code:
conda create -n meu-ambiente python=3.8
conda activate meu-ambiente
Instale as dependências do projeto:

bash
Copy code:
pip install -r requirements.txt
Uso
Inicie a aplicação FastAPI:

bash
Copy code:
uvicorn main:app --reload
A aplicação será executada em http://localhost:8000 por padrão.

Abra seu navegador e acesse a interface da API em http://localhost:8000.

Insira seu nome e as palavras-chave que deseja pesquisar nas vagas de emprego.

Clique no botão "Buscar Vagas".

Os resultados da pesquisa serão exibidos em formato JSON.

## Rotas
/: Página inicial da API com um formulário HTML para pesquisa de vagas.
/vagas/: Rota POST para buscar vagas com base nos critérios de pesquisa. Os resultados são retornados em JSON.
Exemplo de Requisição POST
Você pode fazer uma requisição POST para a rota /vagas/ com o seguinte corpo:

# json
Copy code
{
    "name": "Seu Nome",
    "palavras_chave": ["Python", "Desenvolvedor"]
}
Isso retornará um JSON com as vagas correspondentes às palavras-chave especificadas.