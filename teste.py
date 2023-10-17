import requests
import math
from bs4 import BeautifulSoup

urls = [
   'https://www.zoom.com.br/search?q=jogos%20ps4',
   'https://www.zoom.com.br/search?q=jogos de xbox',
   'https://www.zoom.com.br/search?q=jogos de %20nintendo%20',
]
linkAnuncio = []
totalItems = []

for url in urls:
   webpage = requests.get(url)
   soup = BeautifulSoup(webpage.content, "html.parser")
   anuncios = soup.find_all("a",class_="ProductCard_ProductCard_Inner__tsD4M")

   
   for anuncio in anuncios:
       linkAnuncio.append("https://www.zoom.com.br" +anuncio.get('href'))

for link in linkAnuncio:
   print(link)
   item = {}
   v = requests.get(link)
   soup2 = BeautifulSoup(v.content, "html.parser")
   

   nome = soup2.find("h1").text
   preco = soup2.find("strong" ,attrs={"class":"Text_Text__h_AF6 Text_DesktopHeadingM__C_e4f"}).text

   totalItems.append({
      'nome': nome,
      'precoTotal': preco,
      'precoDesconto': 0,
      'plataforma': "PlayStation",
      'midia': 1,
      'link': link
   })


print(len(totalItems),totalItems[0])

