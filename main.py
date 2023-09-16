import requests 
from bs4 import BeautifulSoup

url_base = "https://www.zoom.com.br/"

produto_name = input("Qual produto voce deseja?: ")

response= requests.get(url_base + "search?q=" + produto_name)

site = BeautifulSoup(response.text, "html.parser")

produto = site.find("a", attrs={"class": "ProductCard_ProductCard_Inner__tsD4M"})

titulo = produto.find("h2",attrs={"class":"Text_Text__h_AF6 Text_MobileLabelXs__ER_cD Text_DesktopLabelSAtLarge__baj_g ProductCard_ProductCard_Name__LT7hv"} )

# link = produto.find("a",attrs={"class":"ProductCard_ProductCard_Inner__tsD4M"})

real = produto.find("p" ,attrs={"class":"Text_Text__h_AF6 Text_MobileHeadingS__Zxam2"})
centavo = produto.find()
print(produto.prettify())
print("Titulo do produto: ",titulo.text)
# print("link do produto: ",link["href"])
