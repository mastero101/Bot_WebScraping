from cgitb import text
import requests
import re
import string
from bs4 import BeautifulSoup
import time
import webbrowser
from sys import argv
from time import sleep

from origamibot import OrigamiBot as Bot
from origamibot.listener import Listener


url = requests.get("https://www.cyberpuerta.mx/Computo-Hardware/Componentes/Procesadores/Procesadores-para-PC/Procesador-AMD-Ryzen-5-5600-S-AM4-3-50GHz-Six-Core-32MB-L3-Cache-con-Disipador-Wraith-Stealth.html")

soup = BeautifulSoup(url.content, "html.parser")
resultado = soup.find("span", {"class": "priceText"})
precioInicio_text = resultado.text
precio = re.sub("\$|\,|","", precioInicio_text)
print(precio)
precioInit = float(precio)

class BotsCommands:
    def __init__(self, bot: Bot,):  # Can initialize however you like
        self.bot = bot

    def start(self, message):   # /start command
        self.bot.send_message(
            message.chat.id,
            'Hello user!\nThis is a Price Checker for your favorite store\n /url "link" to add the link to the article \n /price "XXXX" to set the exprected price')

    def echo(self, message, value: str):  # /echo [value: str] command
        self.bot.send_message(
            message.chat.id,
            value
            )

    def add(self, message, a: float, b: float):  # /add [a: float] [b: float]
        self.bot.send_message(message.chat.id,str(a + b))

    def price(self, message, price: float): # /add expected Price
        if precioInit < price:
            self.bot.send_message(message.chat.id,f"Offer, The price downs to:\n {'$ '+str(precioInit)}\nLink: https://www.cyberpuerta.mx/Computo-Hardware/Componentes/Procesadores/Procesadores-para-PC/Procesador-AMD-Ryzen-5-5600-S-AM4-3-50GHz-Six-Core-32MB-L3-Cache-con-Disipador-Wraith-Stealth.html")
        else:
            self.bot.send_message(message.chat.id,"No Offer")

    def url(self, message, urlGet: str): # /add url
        self.bot.send_message(message.chat.id,"URL Guardada")

    def _not_a_command(self):   # This method not considered a command
        print('I am not a command')

if __name__ == '__main__':
    bot_token = '5627768852:AAH5afLkApzk_l3r8NQWqDtaPUkHAMeE-bA'
    token = (argv[1] if len(argv) > 1 else bot_token)
    bot = Bot(token)   # Create instance of OrigamiBot class

    # Add a command holder
    bot.add_commands(BotsCommands(bot))

    # We can add as many command holders
    # and event listeners as we like

    bot.start()   # start bot's threads
    while True:
        sleep(1)
        # Can also do some useful work i main thread
        # Like autoposting to channels for example


