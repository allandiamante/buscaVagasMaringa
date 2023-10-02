from typing import Union
import utils as utils
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class Vagas(BaseModel):
    name: str   
    palavras_chave: list

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitações de qualquer origem
    allow_methods=["GET", "POST", "OPTIONS"],  # Permitir métodos GET, POST e OPTIONS
)


@app.options("/vagas/")
async def options_vagas():
    allowed_methods = ["GET", "POST", "OPTIONS"]
    response_headers = {
        "Allow": ", ".join(allowed_methods)
    }
    return JSONResponse(
        status_code=200,
        content={},
        headers=response_headers
    )

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("index.html", "r") as file:
        html_content = file.read()
    return html_content

@app.get("/")
def read_root():
    with open("index.html", "r") as file:
        html_content = file.read()
    return html_content

@app.post("/vagas/",)
async def busca_vagas(vagas: Vagas):
    print('POST Busca Vagas')
    print(vagas.name)
    print(vagas.palavras_chave)
    url = "https://empregos.maringa.com/?vagas-de-emprego=1"
    palavra_procurada = vagas.palavras_chave
    lista_itens = utils.pegar_conteudo(url)
    lista_busca = utils.pega_vagas(lista_itens, palavra_procurada)
    utils.printar_itens(lista_busca, len(lista_busca))
    dict_busca = {}
    dict_busca['name'] = vagas.name
    dict_busca['vagas'] = []
    dict_busca['url_vagas'] = []
    for i in range(len(lista_busca)):
        dict_busca['vagas'].append(lista_busca[i].get('title'))
        dict_busca['url_vagas'].append(lista_busca[i].find('a')['href'])    
    dict_busca['quantidade_vaga'] = len(dict_busca['vagas'])
    if dict_busca['quantidade_vaga'] > 0:
        print("------------Vaga index 0-------------")
        print(dict_busca['vagas'][0])
        print(dict_busca['url_vagas'][0])
    return dict_busca