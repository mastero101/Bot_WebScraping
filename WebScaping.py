import re
import string
from bs4 import BeautifulSoup
import requests
import time
import webbrowser

url = requests.get("https://www.cyberpuerta.mx/Computo-Hardware/Componentes/Procesadores/Procesadores-para-PC/Procesador-AMD-Ryzen-5-5600-S-AM4-3-50GHz-Six-Core-32MB-L3-Cache-con-Disipador-Wraith-Stealth.html")

soup = BeautifulSoup(url.content, "html.parser")
resultado = soup.find("span", {"class": "priceText"})
precioInicio_text = resultado.text
precio = re.sub("\$|\,|","", precioInicio_text)
print(precio)
precioInicial = float(precio)

precioDeseado = 2700

if precioInicial < precioDeseado:
    print("Hay Oferta")
else:
    print("No hay Oferta")
