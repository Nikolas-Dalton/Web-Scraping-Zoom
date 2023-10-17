import requests
import math
from bs4 import BeautifulSoup
from lxml import etree

urls = 'https://www.zoom.com.br/search?q=jogos de xbox'


linkAnuncio = []
totalItems = []


webpage = requests.get(urls)
soup = BeautifulSoup(webpage.content, "html.parser")
anuncios = soup.find_all("a",class_="ProductCard_ProductCard_Inner__tsD4M")


for anuncio in anuncios:
    linkAnuncio.append("https://www.zoom.com.br" + anuncio.get('href'))

for link in linkAnuncio:
    # print(link)
    item = {}
    v = requests.get(link)
    soup2 = BeautifulSoup(v.content, "html.parser")
    dom = etree.HTML(str(soup2))
    # print(dom.xpath("//strong[contains(text(), 'R$')]"))


    nome = soup2.find("h1").text
    # print(nome)
    preco = dom.xpath('//strong[contains(text(), "R$")]')[0].text

    totalItems.append({
        'nome': nome,
        'precoTotal': preco,
        'precoDesconto': 0,
        'plataforma': "Xbox",
        'midia': 1,
        'link': link
    })


print(len(totalItems),totalItems[0])

