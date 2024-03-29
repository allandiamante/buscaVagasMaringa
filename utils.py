import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math


def printar_itens(lista_itens, x):
    for i in range(x):
        print(lista_itens[i].get('title'))

def pegar_conteudo(url):
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \ (KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    qtd_itens = soup.find_all('div', class_="card card-anuncio mb-3")
    lista_itens = qtd_itens
    return lista_itens

def verificar_palavra_em_string(palavras, texto):
    texto_lower = texto.lower()  # Convertendo o texto para minúsculas
    for palavra in palavras:
        if palavra.lower() in texto_lower:
            return True
    return False

def pega_vagas(lista_itens, palavra_procurada):    
    lista_vagas = []
    for i in range(len(lista_itens)):
        if verificar_palavra_em_string(palavra_procurada, lista_itens[i].get('title')):            
            lista_vagas.append(lista_itens[i])
    
    
    return lista_vagas
