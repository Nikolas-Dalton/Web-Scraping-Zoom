import requests 
import math
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chomeService
from selenium.webdriver.chrome.options import Options as ChomeOptions


url_base = "https://www.zoom.com.br/"

 
produto_name = []
response= requests.get(url_base + "search?q=" + produto_name) 
site = BeautifulSoup(response.text, "html.parser")


qtd_itens = site.find("div",attrs={"class":"SearchFilters_HitsCount__tyHIc"}).get_text().strip()

qtd_split = qtd_itens.split()[-2]

ultima_pagina = math.ceil(int(qtd_split)/ 24)
# dict_produtos = {'jogo':[], 'preço':[]}

produtos = site.findAll("a", attrs={"class": "ProductCard_ProductCard_Inner__tsD4M"})

for i in range(1,ultima_pagina + 1):
    url_pag = f'https://www.zoom.com.br/search?q={produto_name}&page={i}'
    produto_name = input("Qual produto voce deseja?: ")
    response= requests.get(url_base + "search?q=" + produto_name) 
    # site = BeautifulSoup(response.text, "html.parser")
    produto = site.find_all("div", class_=re.compile("producyCard") )

for produto in produtos:
    titulo = produto.find("h2",attrs={"class":"Text_Text__h_AF6 Text_MobileLabelXs__ER_cD Text_DesktopLabelSAtLarge__baj_g ProductCard_ProductCard_Name__LT7hv"} )
    # link = produto.find("a",attrs={"class":"ProductCard_ProductCard_Inner__tsD4M"})

    real = produto.find("p" ,attrs={"class":"Text_Text__h_AF6 Text_MobileHeadingS__Zxam2"})

    # print(produto.prettify())
    print("Titulo do produto: ",titulo.text)
    print("preço do produto: R$",real.text)
    # print("link do produto: ",link["href"])
    # print(qtd_itens)
    print(qtd_split)
    print("\n\n")